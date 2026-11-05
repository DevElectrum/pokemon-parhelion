ParhelionHomestead_MapScripts::
	.byte 0

ParhelionHomestead_EventScript_FallenTree::
	lock
	msgbox ParhelionHomestead_Text_FallenTree, MSGBOX_DEFAULT
	release
	end

ParhelionHomestead_Text_FallenTree:
	.string "Storm-fallen trees block the\nroad to town.$"
