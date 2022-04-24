#############################################################################
# Generated by PAGE version 7.3
#  in conjunction with Tcl version 8.6
#  Apr 25, 2022 12:36:26 AM CEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m46" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 649x520+517+178
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 7444 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Tiny Tina's Wonderlands - Kadala !"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra46 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 500 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 360 
    vTcl:DefineAlias "$top.fra46" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra46
    labelframe $site_3_0.lab50 \
        -font TkDefaultFont -foreground black -text Offhand \
        -background $vTcl(actual_gui_bg) -height 315 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 90 
    vTcl:DefineAlias "$site_3_0.lab50" "Labelframe3" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab50
    button $site_4_0.but70 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_offhand \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but70" "Button4" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab46 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None -wraplength 1 
    vTcl:DefineAlias "$site_4_0.lab46" "label_melee" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but70 \
        -in $site_4_0 -x 20 -y 270 -anchor nw -bordermode ignore 
    place $site_4_0.lab46 \
        -in $site_4_0 -x 25 -y 17 -width 25 -relwidth 0 -height 241 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab51 \
        -font TkDefaultFont -foreground black -text {Weapon 1} \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 220 
    vTcl:DefineAlias "$site_3_0.lab51" "Labelframe4" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab51
    button $site_4_0.but71 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_weapon_1 \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but71" "Button4_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None 
    vTcl:DefineAlias "$site_4_0.lab47" "label_w1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but71 \
        -in $site_4_0 -x 90 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab47 \
        -in $site_4_0 -x 5 -y 17 -width 205 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab52 \
        -font TkDefaultFont -foreground black -text {Weapon 2} \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 220 
    vTcl:DefineAlias "$site_3_0.lab52" "Labelframe4_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab52
    button $site_4_0.but72 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_weapon_2 \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but72" "Button4_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None 
    vTcl:DefineAlias "$site_4_0.lab48" "label_w2" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but72 \
        -in $site_4_0 -x 90 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab48 \
        -in $site_4_0 -x 5 -y 17 -width 205 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab53 \
        -font TkDefaultFont -foreground black -text {Weapon 3} \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 220 
    vTcl:DefineAlias "$site_3_0.lab53" "Labelframe4_1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab53
    button $site_4_0.but73 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_weapon_3 \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but73" "Button4_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None 
    vTcl:DefineAlias "$site_4_0.lab49" "label_w3" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but73 \
        -in $site_4_0 -x 90 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab49 \
        -in $site_4_0 -x 10 -y 20 -width 205 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab54 \
        -font TkDefaultFont -foreground black -text {Weapon 4} \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 220 
    vTcl:DefineAlias "$site_3_0.lab54" "Labelframe4_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab54
    button $site_4_0.but74 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_weapon_4 \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but74" "Button4_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None 
    vTcl:DefineAlias "$site_4_0.lab50" "label_w4" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but74 \
        -in $site_4_0 -x 90 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab50 \
        -in $site_4_0 -x 5 -y 17 -width 205 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab56 \
        -font TkDefaultFont -foreground black -text {Ring 1} \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 100 
    vTcl:DefineAlias "$site_3_0.lab56" "Labelframe4_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab56
    button $site_4_0.but76 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_ring_1 \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but76" "Button4_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab51 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None 
    vTcl:DefineAlias "$site_4_0.lab51" "label_r1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but76 \
        -in $site_4_0 -x 30 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab51 \
        -in $site_4_0 -x 5 -y 17 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab59 \
        -font TkDefaultFont -foreground black -text Shield \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 100 
    vTcl:DefineAlias "$site_3_0.lab59" "Labelframe4_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab59
    button $site_4_0.but77 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_shield \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but77" "Button4_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab46 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text None 
    vTcl:DefineAlias "$site_4_0.lab46" "label_shield" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but77 \
        -in $site_4_0 -x 30 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab46 \
        -in $site_4_0 -x 5 -y 17 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab60 \
        -font TkDefaultFont -foreground black -text Amulet \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 100 
    vTcl:DefineAlias "$site_3_0.lab60" "Labelframe4_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab60
    button $site_4_0.but78 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_amulet \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but78" "Button4_1_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab47 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text None 
    vTcl:DefineAlias "$site_4_0.lab47" "label_amulet" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but78 \
        -in $site_4_0 -x 30 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab47 \
        -in $site_4_0 -x 5 -y 17 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab62 \
        -font TkDefaultFont -foreground black -text {Ring 2} \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 100 
    vTcl:DefineAlias "$site_3_0.lab62" "Labelframe4_1_1_1_1_2" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab62
    button $site_4_0.but79 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_ring_2 \
        -compound left -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but79" "Button4_1_1_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None 
    vTcl:DefineAlias "$site_4_0.lab52" "label_r2" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but79 \
        -in $site_4_0 -x 30 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab52 \
        -in $site_4_0 -x 5 -y 17 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab63 \
        -font TkDefaultFont -foreground black -text Mod \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 100 
    vTcl:DefineAlias "$site_3_0.lab63" "Labelframe4_1_1_1_1_2_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab63
    button $site_4_0.but80 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_mod -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but80" "Button4_1_1_1_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab48 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text None 
    vTcl:DefineAlias "$site_4_0.lab48" "label_mod" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but80 \
        -in $site_4_0 -x 30 -y 40 -width 42 -height 24 -anchor nw \
        -bordermode ignore 
    place $site_4_0.lab48 \
        -in $site_4_0 -x 5 -y 17 -anchor nw -bordermode ignore 
    labelframe $site_3_0.lab64 \
        -font TkDefaultFont -foreground black -text Spell \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 100 
    vTcl:DefineAlias "$site_3_0.lab64" "Labelframe4_1_1_1_1_2_1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_4_0 $site_3_0.lab64
    button $site_4_0.but81 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command select_spell -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Select 
    vTcl:DefineAlias "$site_4_0.but81" "Button4_1_1_1_1_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_4_0.lab49 \
        -anchor w -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) -text None 
    vTcl:DefineAlias "$site_4_0.lab49" "label_spell" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_0.but81 \
        -in $site_4_0 -x 30 -y 40 -width 42 -relwidth 0 -height 24 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_4_0.lab49 \
        -in $site_4_0 -x 5 -y 17 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 20 -y 10 -width 90 -relwidth 0 -height 315 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab51 \
        -in $site_3_0 -x 120 -y 10 -width 220 -relwidth 0 -height 75 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 120 -y 90 -width 220 -height 75 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 120 -y 170 -width 220 -height 75 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 120 -y 250 -width 220 -height 75 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 20 -y 330 -width 100 -relwidth 0 -height 75 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab59 \
        -in $site_3_0 -x 130 -y 330 -width 100 -height 75 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab60 \
        -in $site_3_0 -x 240 -y 330 -width 100 -height 75 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 20 -y 410 -width 100 -height 75 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab63 \
        -in $site_3_0 -x 130 -y 410 -width 100 -height 75 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab64 \
        -in $site_3_0 -x 240 -y 410 -width 100 -height 75 -anchor nw \
        -bordermode ignore 
    labelframe $top.lab66 \
        -font TkDefaultFont -foreground black -text Target \
        -background $vTcl(actual_gui_bg) -height 75 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 260 
    vTcl:DefineAlias "$top.lab66" "Labelframe5" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab66
    label $site_3_0.lab82 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text None 
    vTcl:DefineAlias "$site_3_0.lab82" "label_from" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command del_from -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Clear 
    vTcl:DefineAlias "$site_3_0.but46" "Button1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab82 \
        -in $site_3_0 -x 20 -y 30 -width 164 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 190 -y 30 -anchor nw -bordermode ignore 
    button $top.but68 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command gamble -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text Gamble 
    vTcl:DefineAlias "$top.but68" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command load_save -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Browse 
    vTcl:DefineAlias "$top.but49" "Button3_1" vTcl:WidgetProc "Toplevel1" 1
    labelframe $top.lab50 \
        -font TkDefaultFont -foreground black -text {Character name} \
        -background $vTcl(actual_gui_bg) -height 55 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 240 
    vTcl:DefineAlias "$top.lab50" "Labelframe1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab50
    entry $site_3_0.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -state readonly -textvariable text_name \
        -width 214 
    vTcl:DefineAlias "$site_3_0.ent51" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent51 \
        -in $site_3_0 -x 10 -y 20 -width 214 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    label $top.lab46 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Waiting... 
    vTcl:DefineAlias "$top.lab46" "label_status" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m46 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    labelframe $top.lab48 \
        -font TkDefaultFont -foreground black -text {Gold available} \
        -background $vTcl(actual_gui_bg) -height 55 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 240 
    vTcl:DefineAlias "$top.lab48" "Labelframe1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab48
    entry $site_3_0.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -state readonly -textvariable text_gold \
        -width 214 
    vTcl:DefineAlias "$site_3_0.ent51" "Entry1_1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent51 \
        -in $site_3_0 -x 10 -y 20 -width 214 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab51 \
        -font TkDefaultFont -foreground black -text Price \
        -background $vTcl(actual_gui_bg) -height 55 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 240 
    vTcl:DefineAlias "$top.lab51" "Labelframe1_1_1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.lab51
    entry $site_3_0.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -state readonly -textvariable text_price \
        -width 214 
    vTcl:DefineAlias "$site_3_0.ent51" "Entry1_1_1" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent51 \
        -in $site_3_0 -x 10 -y 20 -width 214 -relwidth 0 -height 20 \
        -relheight 0 -anchor nw -bordermode ignore 
    button $top.but54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command save_to -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -state disabled -text {Save to} 
    vTcl:DefineAlias "$top.but54" "Button3_2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 0 -textvariable label_gambled 
    vTcl:DefineAlias "$top.lab49" "Label1" vTcl:WidgetProc "Toplevel1" 1
    set label_gambled {0}
    label $top.lab52 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Items gambled} 
    vTcl:DefineAlias "$top.lab52" "Label2" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra46 \
        -in $top -x 10 -y 10 -width 360 -relwidth 0 -height 500 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 380 -y 170 -width 240 -relwidth 0 -height 75 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but68 \
        -in $top -x 380 -y 320 -width 243 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 380 -y 10 -width 243 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 380 -y 50 -width 240 -relwidth 0 -height 55 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 480 -y 480 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 380 -y 110 -width 240 -height 55 -anchor nw \
        -bordermode ignore 
    place $top.lab51 \
        -in $top -x 380 -y 250 -width 240 -height 55 -anchor nw \
        -bordermode ignore 
    place $top.but54 \
        -in $top -x 380 -y 410 -width 243 -relwidth 0 -height 64 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 580 -y 360 -width 22 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 380 -y 360 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

