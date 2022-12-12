#  Copyright 2022 Erik Edin
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import unittest
import makenian

class TestDistance(unittest.TestCase):
    def test_WordDATORSPEL_PuzzleDATORSPEL_DistanceIsZero(self):
        # Arrange

        # Act
        distance = makenian.find_distance("DATORSPEL", "DATORSPEL")

        # Assert
        self.assertEqual(0, distance)