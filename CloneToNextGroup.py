import sublime, sublime_plugin

# Clone the current view to the next group.
# It will create a new group, if there's only one group in the current window.
class CloneToNextGroupCommand(sublime_plugin.WindowCommand):
	def run(self):
		activeWindow = self.window
		whichGroup = activeWindow.active_group() + 1
		currentPoint = self.getCurrentPoint()

		if(activeWindow.num_groups() == 1):
			# Create a new group
			activeWindow.run_command('set_layout', { "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]})

		# If already in the last group, select first one clone the view
		if(whichGroup > activeWindow.num_groups() - 1):
			whichGroup = 0

		activeWindow.run_command('clone_file')
		activeWindow.run_command("move_to_group", { "group": whichGroup })
		self.gotoLine(currentPoint);

	# Return the point in the current view (row, col)
	def getCurrentPoint(self):
		region = self.window.active_view().sel()[0]
		return region.begin()

	def gotoLine(self, point):
		activeView = self.window.active_view()
		activeView.sel().clear()
		activeView.sel().add(sublime.Region(point))
		activeView.show(sublime.Region(point))

