import WPSTemplateMaster

if __name__ == '__main__':
    wps_template_master = WPSTemplateMaster.WPSTemplateMaster('et')
    wps_template_master.remove_all_categories()
    wps_template_master = WPSTemplateMaster.WPSTemplateMaster('wps')
    wps_template_master.remove_all_categories()
    wps_template_master = WPSTemplateMaster.WPSTemplateMaster('wpp')
    wps_template_master.remove_all_categories()
