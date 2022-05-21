import pcbnew
import os

def log(message):
    with open("/Users/chris/pythonlog.txt","a") as writer:
        writer.write(message)

class DeleteTracksPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Delete tracks"
        self.category = "Delete"
        self.description = "Deletes all non locked tracks from the board"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        log("Start\n")

        board = pcbnew.GetBoard()
        tracks = board.GetTracks()

        for track in tracks:
            if track.IsLocked() == False:
                board.Remove(track)

        # zones = board.GetZoneList(False)
        # # for zone in zones:
        # log(str(zones))
        # log(zones.pop())

        log("Done\n")
