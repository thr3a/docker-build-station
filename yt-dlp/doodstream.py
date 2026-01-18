import random
import re
import string
import time
from urllib.parse import urljoin

from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import ExtractorError


class DoodStreamIE(InfoExtractor):
    _VALID_URL = r'''(?x)
        https?://
        (?P<domain>(?:[\w-]+\.)*(?:dood(?:stream)?|d-?s|myvidplay)[\w-]*\.[a-z]{2,})
        /
        (?P<kind>[def])
        /
        (?P<id>[\w-]+)
    '''
    _TESTS = [{
        'url': 'https://d-s.io/e/abc123xyz',
        'only_matching': True,
    }, {
        'url': 'https://dood.pm/d/abc123xyz',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        mobj = self._match_valid_url(url)
        video_id = mobj.group('id')
        kind = mobj.group('kind')

        embed_url = re.sub(r'/(?:d|f)/', '/e/', url, count=1) if kind != 'e' else url
        referer_headers = {'Referer': embed_url}

        webpage = self._download_webpage(embed_url, video_id, headers=referer_headers)

        pass_md5_path = self._search_regex(
            r'(?s)/pass_md5/([^"\']+)',
            webpage,
            'pass_md5 path',
            default=None,
        )
        if not pass_md5_path:
            raise ExtractorError('Unable to locate pass_md5 endpoint', expected=True)

        pass_md5_url = urljoin(embed_url, f'/pass_md5/{pass_md5_path}')

        media_url_base = self._download_webpage(
            pass_md5_url,
            video_id,
            note='Downloading pass_md5 data',
            headers=referer_headers,
        ).strip()

        if not media_url_base:
            raise ExtractorError('Empty media URL received from pass_md5', expected=True)

        token_fragment = pass_md5_path.rsplit('/', 1)[-1]
        token = token_fragment.split('?', 1)[0]

        random_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        expiry = int(time.time())
        final_url = f'{media_url_base}{random_suffix}?token={token}&expiry={expiry}'

        title = (
            self._og_search_title(webpage, default=None)
            or self._html_search_regex(r'<title>([^<]+)</title>', webpage, 'title', default=token)
        )
        thumbnail = self._og_search_thumbnail(webpage)

        formats = [{
            'url': final_url,
            'ext': 'mp4',
            'http_headers': referer_headers,
        }]

        return {
            'id': video_id,
            'title': title,
            'thumbnail': thumbnail,
            'formats': formats,
            'http_headers': referer_headers,
        }
