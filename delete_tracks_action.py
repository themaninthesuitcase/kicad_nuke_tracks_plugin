import pcbnew
import os

class DeleteTracksPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Delete tracks"
        self.category = "Delete"
        self.description = "Deletes all non locked tracks from the board"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        board = pcbnew.GetBoard()
        tracks = board.GetTracks()

        for track in tracks:
            if track.IsLocked() == False:
                board.Remove(track)

        filler = pcbnew.ZONE_FILLER(board)
        filler.Fill(board.Zones())

