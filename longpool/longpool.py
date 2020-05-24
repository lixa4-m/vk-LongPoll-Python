from .config import LONGPOOL_VERSION
import traceback

import requests
import vk
import configs


class even_type(object):
    MESSAGE_NEW = 'message_new'
    MESSAGE_REPLY = 'message_reply'
    MESSAGE_EDIT = 'message_edit'

    MESSAGE_TYPING_STATE = 'message_typing_state'

    MESSAGE_ALLOW = 'message_allow'

    MESSAGE_DENY = 'message_deny'

    PHOTO_NEW = 'photo_new'

    PHOTO_COMMENT_NEW = 'photo_comment_new'
    PHOTO_COMMENT_EDIT = 'photo_comment_edit'
    PHOTO_COMMENT_RESTORE = 'photo_comment_restore'

    PHOTO_COMMENT_DELETE = 'photo_comment_delete'

    AUDIO_NEW = 'audio_new'

    VIDEO_NEW = 'video_new'

    VIDEO_COMMENT_NEW = 'video_comment_new'
    VIDEO_COMMENT_EDIT = 'video_comment_edit'
    VIDEO_COMMENT_RESTORE = 'video_comment_restore'

    VIDEO_COMMENT_DELETE = 'video_comment_delete'

    WALL_POST_NEW = 'wall_post_new'
    WALL_REPOST = 'wall_repost'

    WALL_REPLY_NEW = 'wall_reply_new'
    WALL_REPLY_EDIT = 'wall_reply_edit'
    WALL_REPLY_RESTORE = 'wall_reply_restore'

    WALL_REPLY_DELETE = 'wall_reply_delete'

    BOARD_POST_NEW = 'board_post_new'
    BOARD_POST_EDIT = 'board_post_edit'
    BOARD_POST_RESTORE = 'board_post_restore'

    BOARD_POST_DELETE = 'board_post_delete'

    MARKET_COMMENT_NEW = 'market_comment_new'
    MARKET_COMMENT_EDIT = 'market_comment_edit'
    MARKET_COMMENT_RESTORE = 'market_comment_restore'

    MARKET_COMMENT_DELETE = 'market_comment_delete'

    GROUP_LEAVE = 'group_leave'

    GROUP_JOIN = 'group_join'

    USER_BLOCK = 'user_block'

    USER_UNBLOCK = 'user_unblock'

    POLL_VOTE_NEW = 'poll_vote_new'

    GROUP_OFFICERS_EDIT = 'group_officers_edit'

    GROUP_CHANGE_SETTINGS = 'group_change_settings'

    GROUP_CHANGE_PHOTO = 'group_change_photo'

    VKPAY_TRANSACTION = 'vkpay_transaction'
        
class messages(object):

    def __init__(self, lp):
        self.lp = lp
        self.lp_updates = lp['updates'][0]
        self.lp_type = lp['updates'][0]['type']

    def update(self, all_updates):
        if all_updates: return self.lp_updates
        if LONGPOOL_VERSION == 5.103:
            return self.lp_updates['object']['message']
        else:
            return self.lp_updates['object']

def listen(all_updates=False):
    token = configs.tokens()
    api = vk.API(vk.Session(access_token=token), v=5.103)
    settings = api.groups.getById()
    group_id = settings[0]['id']
    GetInfo = api.groups.getLongPollServer(group_id=group_id)
    key = GetInfo.get('key')
    server = GetInfo.get('server')
    ts = GetInfo.get('ts')
    print('Longpool enabled!')
    while True:
        try:
            lp = requests.get(f'{server}?act=a_check&key={key}&ts={ts}&wait=60').json()
            if lp.get('failed') is not None:
                key = api.groups.getLongPollServer(group_id=group_id, v=5.8)['key']
            if ts != lp.get('ts') and lp.get('updates'):
                if lp['updates'][0]['type'] =='message_new':
                    try:
                        yield messages.update(messages(lp), all_updates)
                    except Exception as e:
                        print(lp)
                        print(traceback.format_exc())

            ts = lp.get('ts')

        except KeyboardInterrupt:
            print('\nExiting...')
            exit(0)

        except Exception as e:
            print(traceback.format_exc())