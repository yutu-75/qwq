# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
import sys

__ROOT__ = os.path.dirname(os.path.abspath(__file__))
__ROOT__ = os.path.join(__ROOT__, "..")
sys.path.append(__ROOT__)

from superset import create_app

# os.environ["superset_dev"] = os.path.join(os.getcwd(), 'superset_dev/Scripts')

if __name__ == '__main__':
    superset_app = create_app()
    superset_app.run(host="0.0.0.0", port="30000", debug=True)
