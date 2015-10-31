# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
           # ypos 993            
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"


            window:
                ypos 315              
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
            
            if who:
                window:
                    xpos 230
                    ypos -125                    
                    style "say_who_window"

                    text who:
                        id "who"                

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 10

            for caption, action, chosen in items:

                if action:

                    button:
                        action action at xfade
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear
        color "#4f3131"

    style menu_choice_button is button:
        xminimum 494
        xmaximum 494
        yminimum 58
        idle_background Frame("GUI/choice.png",28,9)
        hover_background Frame("GUI/choice_hover.png",28,9)

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
    add "GUI/title_frame.png"
    # The main menu buttons.
    hbox:
        xpos 672
        ypos 673
        imagebutton idle "GUI/title_start.png" hover "GUI/title_start_hover.png" action Start() at ttfade
    hbox:
        xpos 788
        ypos 673
        imagebutton idle "GUI/title_load.png" hover "GUI/title_load_hover.png" action ShowMenu("main_load") at ttfade
    hbox:
        xpos 904
        ypos 673
        imagebutton idle "GUI/title_pref.png" hover "GUI/title_pref_hover.png" action ShowMenu("main_preferences") at ttfade
    hbox:
        xpos 1155
        ypos 673
        imagebutton idle "GUI/title_quit.png" hover "GUI/title_quit_hover.png" action Quit() at ttfade  

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen load_save_slot:
    #tag menu
    #modal True
#    $ file_text = "%2s. %s\n  %s" % (
#                        FileSlotName(number, 4),
#                        FileTime(number, empty=_("Empty Slot")),
#                        FileSaveName(number))

    add FileScreenshot(number) xpos 11 ypos 11
#    text file_text xalign .5 yalign 10.0 
                    
screen save:

    # This ensures that any other menu screen is replaced.
    tag menu
    add "GUI/base.png"
    imagemap:
        alpha False
        ground "GUI/slots.png"
        idle "GUI/idle.png"
        hover "GUI/slots.png"
        insensitive "GUI/idle.png"
            
        hotspot (202, 94, 441, 258) at slotfade clicked FileAction(1):
            use load_save_slot(number=1)
        hotspot (725, 94, 441, 258) at slotfade clicked FileAction(2):
            use load_save_slot(number=2)
        hotspot (202, 400, 441, 258) at slotfade clicked FileAction(3):
            use load_save_slot(number=3)     
        hotspot (725, 400, 441, 258) at slotfade clicked FileAction(4):
            use load_save_slot(number=4)   
              
        hotspot (563, 728, 77, 29) at textfade clicked FilePage("auto")
        hotspot (652, 728, 24, 29) at textfade clicked FilePage("1")
        hotspot (681, 728, 24, 29) at textfade clicked FilePage("2")   
        hotspot (716, 728, 24, 29) at textfade clicked FilePage("3")
        hotspot (750, 728, 24, 29) at textfade clicked FilePage("4")
        hotspot (784, 728, 24, 29) at textfade clicked FilePage("5")

    imagebutton idle "GUI/button_x.png" hover "GUI/button_x.png" xpos 1281 ypos 34 focus_mask True action Return() at xfade

    hbox:
        xpos 405
        ypos 9
        imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" selected_idle "GUI/button_save_hover.png" selected_hover "GUI/button_save_hover.png" action ShowMenu("save") at xfade
    hbox:
        xpos 498
        ypos 9
        imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" selected_idle "GUI/button_load_hover.png" selected_hover "GUI/button_load_hover.png"  action ShowMenu("load") at xfade
    hbox:
        xpos 596
        ypos 9
        imagebutton idle "GUI/button_pref.png" hover "GUI/button_pref_hover.png" selected_idle "GUI/button_pref_hover.png" selected_hover "GUI/button_pref_hover.png"  action ShowMenu("preferences") at xfade

    hbox:
        xpos 809
        ypos 9
        imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" selected_idle "GUI/button_main_hover.png" selected_hover "GUI/button_main_hover.png" action MainMenu() at xfade
    hbox:
        xpos 903
        ypos 9
        imagebutton idle "GUI/button_quit.png" hover "GUI/button_quit_hover.png" selected_idle "GUI/button_quit_hover.png" selected_hover "GUI/button_quit_hover.png" action Quit() at xfade 

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu
    add "GUI/base.png"
    imagemap:
        alpha False
        ground "GUI/slots.png"
        idle "GUI/idle.png"
        hover "GUI/slots.png"
        insensitive "GUI/idle.png"
            
        hotspot (202, 94, 441, 258) at slotfade clicked FileAction(1):
            use load_save_slot(number=1)
        hotspot (725, 94, 441, 258) at slotfade clicked FileAction(2):
            use load_save_slot(number=2)
        hotspot (202, 400, 441, 258) at slotfade clicked FileAction(3):
            use load_save_slot(number=3)     
        hotspot (725, 400, 441, 258) at slotfade clicked FileAction(4):
            use load_save_slot(number=4)   
              
        hotspot (563, 728, 77, 29) at textfade clicked FilePage("auto")
        hotspot (652, 728, 24, 29) at textfade clicked FilePage("1")
        hotspot (681, 728, 24, 29) at textfade clicked FilePage("2")   
        hotspot (716, 728, 24, 29) at textfade clicked FilePage("3")
        hotspot (750, 728, 24, 29) at textfade clicked FilePage("4")
        hotspot (784, 728, 24, 29) at textfade clicked FilePage("5")

    imagebutton idle "GUI/button_x.png" hover "GUI/button_x.png" xpos 1281 ypos 34 focus_mask True action Return() at xfade

    hbox:
        xpos 405
        ypos 9
        imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" selected_idle "GUI/button_save_hover.png" selected_hover "GUI/button_save_hover.png" action ShowMenu("save") at xfade
    hbox:
        xpos 498
        ypos 9
        imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" selected_idle "GUI/button_load_hover.png" selected_hover "GUI/button_load_hover.png"  action ShowMenu("load") at xfade
    hbox:
        xpos 596
        ypos 9
        imagebutton idle "GUI/button_pref.png" hover "GUI/button_pref_hover.png" selected_idle "GUI/button_pref_hover.png" selected_hover "GUI/button_pref_hover.png"  action ShowMenu("preferences") at xfade

    hbox:
        xpos 809
        ypos 9
        imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" selected_idle "GUI/button_main_hover.png" selected_hover "GUI/button_main_hover.png" action MainMenu() at xfade
    hbox:
        xpos 903
        ypos 9
        imagebutton idle "GUI/button_quit.png" hover "GUI/button_quit_hover.png" selected_idle "GUI/button_quit_hover.png" selected_hover "GUI/button_quit_hover.png" action Quit() at xfade  


screen main_load:

    # This ensures that any other menu screen is replaced.
    tag menu
    add "GUI/title.png"
    add "GUI/base.png"
    imagemap:
        alpha False
        ground "GUI/slots.png"
        idle "GUI/idle.png"
        hover "GUI/slots.png"
        insensitive "GUI/idle.png"
            
        hotspot (202, 94, 441, 258) at slotfade clicked FileLoad(1):
            use load_save_slot(number=1)
        hotspot (725, 94, 441, 258) at slotfade clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (202, 400, 441, 258) at slotfade clicked FileLoad(3):
            use load_save_slot(number=3)     
        hotspot (725, 400, 441, 258) at slotfade clicked FileLoad(4):
            use load_save_slot(number=4)   
              
        hotspot (563, 728, 77, 29) at textfade clicked FilePage("auto")
        hotspot (652, 728, 24, 29) at textfade clicked FilePage("1")
        hotspot (681, 728, 24, 29) at textfade clicked FilePage("2")   
        hotspot (716, 728, 24, 29) at textfade clicked FilePage("3")
        hotspot (750, 728, 24, 29) at textfade clicked FilePage("4")
        hotspot (784, 728, 24, 29) at textfade clicked FilePage("5")

    imagebutton idle "GUI/button_x.png" hover "GUI/button_x.png" xpos 1281 ypos 34 focus_mask True action Return() at xfade

    hbox:
        xpos 405
        ypos 9
        imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" selected_idle "GUI/button_save_hover.png" selected_hover "GUI/button_save_hover.png" action ShowMenu("save") at xfade
    hbox:
        xpos 498
        ypos 9
        imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" selected_idle "GUI/button_load_hover.png" selected_hover "GUI/button_load_hover.png"  action ShowMenu("main_load") at xfade
    hbox:
        xpos 596
        ypos 9
        imagebutton idle "GUI/button_pref.png" hover "GUI/button_pref_hover.png" selected_idle "GUI/button_pref_hover.png" selected_hover "GUI/button_pref_hover.png"  action ShowMenu("main_preferences") at xfade

    hbox:
        xpos 809
        ypos 9
        imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" selected_idle "GUI/button_main_hover.png" selected_hover "GUI/button_main_hover.png" action Return() at xfade
    hbox:
        xpos 903
        ypos 9
        imagebutton idle "GUI/button_quit.png" hover "GUI/button_quit_hover.png" selected_idle "GUI/button_quit_hover.png" selected_hover "GUI/button_quit_hover.png" action Quit() at xfade  


init -2 python:
    config.thumbnail_width = 415
    config.thumbnail_height = 231
    config.quit_action = Quit(confirm=False)


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    add "GUI/base.png"
    add "GUI/preferences.png"
    
    hbox:
        xpos 180
        ypos 168
        imagebutton idle "GUI/window.png" hover "GUI/window.png" selected_idle "GUI/window_hover.png" selected_hover "GUI/window_hover.png" action Preference("display", "window") at xxfade
        
    hbox:
        xpos 180
        ypos 233
        imagebutton idle "GUI/fullscreen.png" hover "GUI/fullscreen.png" selected_idle "GUI/fullscreen_hover.png" selected_hover "GUI/fullscreen_hover.png" action  Preference("display", "fullscreen") at xxfade
    
    hbox:
        xpos 180
        ypos 328
        imagebutton idle "GUI/seen.png" hover "GUI/seen.png" selected_idle "GUI/seen_hover.png" selected_hover "GUI/seen_hover.png" action Preference("skip", "seen") at xxfade
    hbox:
        xpos 180
        ypos 393
        imagebutton idle "GUI/all.png" hover "GUI/all.png" selected_idle "GUI/all_hover.png" selected_hover "GUI/all_hover.png" action Preference("skip", "all") at xxfade
    hbox:
        xpos 180
        ypos 493
        imagebutton idle "GUI/stop.png" hover "GUI/stop.png" selected_idle "GUI/stop_hover.png" selected_hover "GUI/stop_hover.png" action Preference("after choices", "stop") at xxfade
    hbox:
        xpos 180
        ypos 558
        imagebutton idle "GUI/keep.png" hover "GUI/keep.png" selected_idle "GUI/keep_hover.png" selected_hover "GUI/keep_hover.png" action Preference("after choices", "skip") at xxfade
        

    imagebutton idle "GUI/button_x.png" hover "GUI/button_x.png" xpos 1281 ypos 34 focus_mask True action Return() at xfade
    
    hbox:
        xpos 405
        ypos 9
        imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" selected_idle "GUI/button_save_hover.png" selected_hover "GUI/button_save_hover.png" action ShowMenu("save") at xfade
    hbox:
        xpos 498
        ypos 9
        imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" selected_idle "GUI/button_load_hover.png" selected_hover "GUI/button_load_hover.png"  action ShowMenu("load") at xfade
    hbox:
        xpos 596
        ypos 9
        imagebutton idle "GUI/button_pref.png" hover "GUI/button_pref_hover.png" selected_idle "GUI/button_pref_hover.png" selected_hover "GUI/button_pref_hover.png"  action ShowMenu("preferences") at xfade

    hbox:
        xpos 809
        ypos 9
        imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" selected_idle "GUI/button_main_hover.png" selected_hover "GUI/button_main_hover.png" action MainMenu() at xfade
    hbox:
        xpos 903
        ypos 9
        imagebutton idle "GUI/button_quit.png" hover "GUI/button_quit_hover.png" selected_idle "GUI/button_quit_hover.png" selected_hover "GUI/button_quit_hover.png" action Quit() at xfade 

    vbox:
        style_group "pref"
        
        bar pos (700, 217) value Preference("auto-forward time")
    
    vbox:
        style_group "pref"
        
        bar pos (700, 335) value Preference("text speed")  
    
    vbox:
        style_group "pref"

        bar pos (700, 455) value Preference("music volume")        
   
    vbox:
        style_group "pref"
        
        bar pos (700, 578) value Preference("sound volume")     

 
screen main_preferences():

    tag menu
    add "GUI/title.png"
    add "GUI/base.png"
    add "GUI/preferences.png"
    
    hbox:
        xpos 180
        ypos 168
        imagebutton idle "GUI/window.png" hover "GUI/window.png" selected_idle "GUI/window_hover.png" selected_hover "GUI/window_hover.png" action Preference("display", "window") at xxfade
        
    hbox:
        xpos 180
        ypos 233
        imagebutton idle "GUI/fullscreen.png" hover "GUI/fullscreen.png" selected_idle "GUI/fullscreen_hover.png" selected_hover "GUI/fullscreen_hover.png" action  Preference("display", "fullscreen") at xxfade
    
    hbox:
        xpos 180
        ypos 328
        imagebutton idle "GUI/seen.png" hover "GUI/seen.png" selected_idle "GUI/seen_hover.png" selected_hover "GUI/seen_hover.png" action Preference("skip", "seen") at xxfade
    hbox:
        xpos 180
        ypos 393
        imagebutton idle "GUI/all.png" hover "GUI/all.png" selected_idle "GUI/all_hover.png" selected_hover "GUI/all_hover.png" action Preference("skip", "all") at xxfade
    hbox:
        xpos 180
        ypos 493
        imagebutton idle "GUI/stop.png" hover "GUI/stop.png" selected_idle "GUI/stop_hover.png" selected_hover "GUI/stop_hover.png" action Preference("after choices", "stop") at xxfade
    hbox:
        xpos 180
        ypos 558
        imagebutton idle "GUI/keep.png" hover "GUI/keep.png" selected_idle "GUI/keep_hover.png" selected_hover "GUI/keep_hover.png" action Preference("after choices", "skip") at xxfade
        

    imagebutton idle "GUI/button_x.png" hover "GUI/button_x.png" xpos 1281 ypos 34 focus_mask True action Return() at xfade
    
    hbox:
        xpos 405
        ypos 9
        imagebutton idle "GUI/button_save.png" hover "GUI/button_save_hover.png" selected_idle "GUI/button_save_hover.png" selected_hover "GUI/button_save_hover.png" action ShowMenu("save") at xfade
    hbox:
        xpos 498
        ypos 9
        imagebutton idle "GUI/button_load.png" hover "GUI/button_load_hover.png" selected_idle "GUI/button_load_hover.png" selected_hover "GUI/button_load_hover.png"  action ShowMenu("main_load") at xfade
    hbox:
        xpos 596
        ypos 9
        imagebutton idle "GUI/button_pref.png" hover "GUI/button_pref_hover.png" selected_idle "GUI/button_pref_hover.png" selected_hover "GUI/button_pref_hover.png"  action ShowMenu("main_preferences") at xfade

    hbox:
        xpos 809
        ypos 9
        imagebutton idle "GUI/button_main.png" hover "GUI/button_main_hover.png" selected_idle "GUI/button_main_hover.png" selected_hover "GUI/button_main_hover.png" action Return() at xfade
    hbox:
        xpos 903
        ypos 9
        imagebutton idle "GUI/button_quit.png" hover "GUI/button_quit_hover.png" selected_idle "GUI/button_quit_hover.png" selected_hover "GUI/button_quit_hover.png" action Quit() at xfade 

    vbox:
        style_group "pref"
        
        bar pos (700, 217) value Preference("auto-forward time")
    
    vbox:
        style_group "pref"
        
        bar pos (700, 335) value Preference("text speed")  
    
    vbox:
        style_group "pref"

        bar pos (700, 455) value Preference("music volume")        
   
    vbox:
        style_group "pref"
        
        bar pos (700, 578) value Preference("sound volume")     

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        is default
        xminimum 450
        xmaximum 450
        yminimum 30
        left_bar "GUI/bar.png"
        right_bar "GUI/bar.png"
        thumb "GUI/slider.png"
        left_gutter 61
        right_gutter 60

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    add "GUI/base.png"
    
    imagebutton idle "GUI/button_x.png" hover "GUI/button_x.png" xpos 1281 ypos 34 focus_mask True action no_action at xfade
    
    vbox:
        style_group "yesno"
        xalign .5
        yalign .45
        spacing 30

        label _(message):
            xalign 0.5

        vbox:
            xalign 0.5
            spacing 30
            
            imagebutton idle "GUI/yes.png" hover "GUI/yes_hover.png" action yes_action at xxfade
            imagebutton idle "GUI/no.png" hover "GUI/no_hover.png" action no_action at xxfade


    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 0.98
        yalign 0.997
        
        textbutton _("Auto") action Preference("auto-forward", "toggle") at textfade
        textbutton _("Skip") action Skip() at textfade
        textbutton _("Save") action ShowMenu('save') at textfade
        textbutton _("Load") action ShowMenu('load') at textfade
        textbutton _("Main") action MainMenu() at textfade
        textbutton _("Quit") action Quit() at textfade

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 24
        color "#4f3131"
#        hover_color "#ccc"
#        selected_idle_color "#cc08"
#        selected_hover_color "#cc0"
#        insensitive_color "#4448"
        font "GUI/Bocklin.ttf"
        outlines [(0, "#420202"),(1, "#d5d9b4")]
        drop_shadow_color "#420202"
        drop_shadow (-1, 1)







