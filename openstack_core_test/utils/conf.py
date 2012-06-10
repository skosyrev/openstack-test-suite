# -*- coding: utf-8 -*-
# <Openstack-Test-Suite - integration test suite for Openstack>
# Copyright (c) 2012 Grid Dynamics Consulting Services, Inc, All Rights Reserved
# http://www.griddynamics.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import yaml
import time

#bash_log_file
#env_dir_path

def get_bash_log_file():
    global bash_log_file
    return bash_log_file

def get_debug_log_file():
    global debug_log_file
    return debug_log_file

def init(dir_path):
    print dir_path
    global bash_log_file, env_dir_path, debug_log_file
    env_dir_path = dir_path
    bash_log_file = os.path.join(env_dir_path, "bash.log")
    debug_log_file = os.path.join(env_dir_path, "debug.log")

def load_yaml_config(filename):
    with open(filename, 'r') as config_file:
        config = yaml.load(config_file)
        return config

def log(logfile, message):
    with open(logfile, 'a+b') as file:
        file.write('%s: %s\n' % (time.ctime(), message))

def bash_log(cmd, status, text):
    log(get_bash_log_file(), "[COMMAND] " + cmd)
    log(get_bash_log_file(), "[RETCODE] %s" % status)
    log(get_bash_log_file(), "[OUTPUT]\n %s" % text)

def debug_log(text):
    log(get_debug_log_file(), text)

def get_current_module_path(module_file):
    return os.path.dirname(os.path.abspath(module_file))

