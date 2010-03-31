# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'variables': {
    'apache_sdk_root': '<(DEPTH)/third_party/apache_httpd',
    'apache_sdk_os_root': '<(apache_sdk_root)/arch/<(OS)',
    'apache_sdk_arch_root': '<(apache_sdk_os_root)/<(target_arch)',
  },
  'targets': [
    {
      'target_name': 'apache_httpd',
      'type': 'none',
      'direct_dependent_settings': {
        'include_dirs': [
          '<(apache_sdk_root)/include',
          '<(apache_sdk_os_root)/all/include',
          '<(apache_sdk_arch_root)/include',
        ],
        'conditions': [
          ['OS == "win"', {
            'link_settings': {
              'libraries': [
                '<(apache_sdk_arch_root)/lib/apr-1.lib',
                '<(apache_sdk_arch_root)/lib/aprutil-1.lib',
                '<(apache_sdk_arch_root)/lib/libapr-1.lib',
                '<(apache_sdk_arch_root)/lib/libaprutil-1.lib',
                '<(apache_sdk_arch_root)/lib/libhttpd.lib',
              ],
            },
          }],
          ['OS == "linux"', {
            'defines': [
              # We need to define _LARGEFILE64_SOURCE so <sys/types.h>
              # provides off64_t.
              '_LARGEFILE64_SOURCE',
            ],
          }],
        ],
      },
    },
  ],
}