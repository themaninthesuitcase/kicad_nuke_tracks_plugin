import pcbnew
import os

class NukeTracksPluginAction(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "Nuke Tracks"
        self.category = "Nuke"
        self.description = "Deletes all non locked tracks from the board, then refills the zones."
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

        pcbnew.UpdateUserInterface()

