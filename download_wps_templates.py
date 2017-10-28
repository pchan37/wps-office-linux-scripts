import WPSTemplateDownloader

if __name__ == '__main__':
    wps_template_downloader = WPSTemplateDownloader.WPSTemplateDownloader('et')
    wps_template_downloader.download_all_categories()
    wps_template_downloader = WPSTemplateDownloader.WPSTemplateDownloader('wps')
    wps_template_downloader.download_all_categories()
    wps_template_downloader = WPSTemplateDownloader.WPSTemplateDownloader('wpp')
    wps_template_downloader.download_all_categories()
