import json
from urllib.parse import urljoin

from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.utils import (
    ExtractorError,
    clean_html,
    extract_attributes,
    int_or_none,
)


class DianaLiveIE(InfoExtractor):
    _VALID_URL = r'https?://live\.www-diana\.com/purchased/player/(?P<id>\d+)'
    _TESTS = [{
        'url': 'https://live.www-diana.com/purchased/player/31738',
        'info_dict': {
            'id': '31738',
            'ext': 'mp4',
            'title': r're:.',
        },
        'params': {'skip_download': True},
        'skip': '要ログイン',
    }]

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        csrf_token = self._search_regex(
            r'<meta\s+name=["\']csrf-token["\']\s+content=["\']([^"\']+)',
            webpage, 'CSRF token', default=None)
        if not csrf_token:
            raise ExtractorError('CSRFトークンの取得に失敗しました', expected=True)

        player_tag = self._search_regex(
            r'(<positivesalon-video-player[^>]+>)',
            webpage, 'player component', default=None)
        if not player_tag:
            raise ExtractorError('再生情報が取得できません。ログインが必要です。', expected=True)

        attrs = extract_attributes(player_tag)
        item_id = int_or_none(attrs.get('first_item_id'))
        if not item_id:
            raise ExtractorError('アイテムIDの取得に失敗しました', expected=True)
        digicon_id = int_or_none(attrs.get('first_digicon_id')) or int_or_none(video_id)

        api_headers = {
            'X-CSRF-TOKEN': csrf_token,
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': url,
        }

        detail_headers = api_headers.copy()
        detail_headers['Content-Type'] = 'application/json'
        contents = self._download_json(
            f'https://live.www-diana.com/purchased/digicon/detail/{item_id}',
            video_id, headers=detail_headers,
            data=json.dumps({'type': 'content'}).encode())
        if not isinstance(contents, list):
            raise ExtractorError('コンテンツ情報の形式が不正です', expected=True)

        entry = next(
            (c for c in contents if int_or_none(c.get('digicon_id')) == digicon_id),
            contents[0] if contents else None)
        if not entry:
            raise ExtractorError('対象のコンテンツが見つかりません', expected=True)

        target_digicon_id = entry.get('digicon_id') or digicon_id
        if not target_digicon_id:
            raise ExtractorError('Digicon IDの取得に失敗しました', expected=True)

        media_info = self._download_json(
            f'https://live.www-diana.com/digicon/content/{target_digicon_id}',
            video_id, headers=api_headers)
        media_path = media_info.get('fname')
        if not media_path:
            raise ExtractorError('動画URLの取得に失敗しました', expected=True)

        media_url = urljoin(url, media_path)
        formats = self._extract_m3u8_formats(media_url, video_id, 'mp4', m3u8_id='hls')

        title = (entry.get('item_title') or entry.get('title')
                 or entry.get('title_ja') or entry.get('title_en'))
        if not title:
            title = self._html_search_regex(r'<title>([^<]+)', webpage, 'title', fatal=False)
        description = clean_html(entry.get('item_description')) or self._og_search_description(webpage, default=None)

        item_for_thumb = int_or_none(entry.get('item_id')) or item_id
        thumbnail = urljoin(url, f'/item/image/{item_for_thumb}') if item_for_thumb else None

        return {
            'id': video_id,
            'title': title,
            'description': description,
            'thumbnail': thumbnail,
            'formats': formats,
        }
