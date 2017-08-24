import Queue
import gi

gi.require_version('Playerctl', '1.0')
from gi.repository import Playerctl, GLib

queue = Queue.Queue()
PLAYER_NAMES = ['spotify', 'rhythmbox', 'vlc', ]  # order is important


def get_player():
    for player_name in PLAYER_NAMES:
        player_instance = Playerctl.Player(player_name=player_name)
        if player_instance.props.status is not None:
            return player_instance
    player_instance = Playerctl.Player(player_name=PLAYER_NAMES[0])
    return player_instance


def on_track_change(player, e):
    artist = player.get_artist()
    title = player.get_title()
    print 'Now playing:'
    print '{artist} - {title}'.format(artist=artist, title=title)
    queue.put((artist, title))

player = get_player()