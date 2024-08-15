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

import re


class PasswordStrength:
    def __init__(self, password):
        self.password = password
        self.strength = self.calculate_strength()

    def calculate_strength(self) -> int:
        strength = 0
        if len(self.password) >= 8:
            strength += 1
        if re.search(r"\d", self.password):
            strength += 1
        if re.search(r"[a-z]", self.password):
            strength += 1
        if re.search(r"[A-Z]", self.password):
            strength += 1
        # if re.search(r"[!@#$%^&*()_+-=]", self.password):
        #     self.strength += 1
        return strength

    @property
    def check_pwd_strength(self) -> bool:
        if self.strength == 4:
            return True

        return False
