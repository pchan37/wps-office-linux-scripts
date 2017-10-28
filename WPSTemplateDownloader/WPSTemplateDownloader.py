import os
import re
import subprocess

from lib.utils import file_tools
from lib.utils import interrupt
from lib.utils import web

class WPSTemplateDownloader(object):

    template_type_to_url_ref_and_general_name = {'et': ('spreadsheets', 'Spreadsheets'),
                                                 'wpp': ('ppt', 'PPT'),
                                                 'wps': ('word', 'Writer')}

    def __init__(self, template_type):
        self.homepage = 'http://www.ksosoft.com/'
        self.template_type = template_type
        self.url_reference, self.template_general_name = WPSTemplateDownloader.template_type_to_url_ref_and_general_name[self.template_type]
        self.template_pattern = re.compile('(images/\w+_template/[\w_-]+template/([\w-]+?\d*)\.(dpt|ett|wpt))')

    def not_empty(self, string):
        return string

    def _create_directory(self, category_name):
        DIRECTORY_NAME = category_name.title()
        DIRECTORY_NAME = os.path.join('test', DIRECTORY_NAME)
        file_tools.assure_directory_path_exists(DIRECTORY_NAME)
        return DIRECTORY_NAME

    def _download_template(self, url):
        template_file_content = web.download_page(url)
        return template_file_content

    def _write(self, destination, file_content):
        try:
            with open(destination, 'w') as template_file:
                template_file.write(file_content)
            return True
        except OSError as e:
            print 'Failed to write template file, please check that you have write permissions!'
            raise SystemExit(1)

    def download_category(self, category, call_from_parent=False):
        category_pretty_format = category[:category.find('-ppt')] if category.endswith('-ppt') else category
        DESTINATION_DIRECTORY = self._create_directory(category_pretty_format)
        page_number = 0
        url_template = 'http://www.ksosoft.com/{}-template?page={{}}'.format(category)

        url = url_template.format(page_number)
        templates_url_list = self.template_pattern.findall(web.get_source(url))
        while len(templates_url_list):
            for url_component, filename_without_suffix, suffix in templates_url_list:
                file_content = self._download_template(self.homepage + url_component)
                assert self.not_empty(file_content), 'Error: Unable to download template, {}'.format(filename_without_suffix + suffix)

                with interrupt.KeyboardInterruptBlocked():
                    filename = filename_without_suffix + '.' + suffix
                    DESTINATION = os.path.join(DESTINATION_DIRECTORY, filename)
                    self._write(DESTINATION, file_content)

            page_number += 1
            url = url_template.format(page_number)
            templates_url_list = self.template_pattern.findall(web.get_source(url))
        if not call_from_parent:
            subprocess.call(['sudo', 'cp', '-r', DESTINATION_DIRECTORY, '/opt/kingsoft/wps-office/office6/mui/en_US/templates/{}'.format(self.template_type)])
            subprocess.call(['rm', '-rf', DESTINATION_DIRECTORY])
        return True


    def download_all_categories(self):
        HOMEPAGE = 'http://www.ksosoft.com/{}-template'.format(self.url_reference)
        homepage_content = web.get_source(HOMEPAGE)

        pattern = re.compile('[\w -]+?-template(?!s)(?!-)(?=>)')
        raw_data = pattern.findall(homepage_content)
        section_listing = set(raw_data)

        section_to_category = lambda x: (x[:x.find('template') - 1]).lower()
        category_list = [section_to_category(section) for section in section_listing]

        category_directory_listing = []
        for category in category_list:
            category_pretty_format = category[:category.find('-ppt')] if category.endswith('-ppt') else category
            print 'Downloading {} templates for {}...'.format(category_pretty_format, self.template_type.upper())
            category_url_format ='-'.join(category.split())
            category_directory_name = self.download_category(category_url_format, call_from_parent=True)
            category_directory_listing.append(category_directory_name)
        print 'Finishing up...'
        for directory in category_directory_listing:
            subprocess.call(['sudo', 'cp', '-r', directory, '/opt/kingsoft/wps-office/office6/mui/en_US/templates/{}'.format(self.template_type)])
            subprocess.call(['rm', '-rf', directory])
        print 'Done!'
        return True
