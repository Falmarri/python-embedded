# Copyright (c) 2002-2013 "Neo Technology,"
# Network Engine for Objects in Lund AB [http://neotechnology.com]
#
# This file is part of Neo4j.
#
# Neo4j is free software: you can redistribute it and/or modify
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

#from _backend import extends, implements, rel_type, TraverserImpl,\
#                     Traversal, TraversalDescriptionImpl, strings,\
#                     Evaluation, Evaluator, Uniqueness,\
#                     TraversalBranchImpl, BidirectionalTraversalBranchPath,\
#                     ExtendedPath, SingleNodePath, FinalTraversalBranch,\
#                     AsOneStartBranch, StartNodeTraversalBranch, WrappedPath


from _backend import extends, implements, rel_type, Traversal,\
    TraversalDescription, Evaluation

from util import PythonicIterator
from core import Direction, DirectionalType

# Give the user references to the
# direct evaluator decision choices.
INCLUDE_AND_CONTINUE = Evaluation.INCLUDE_AND_CONTINUE
INCLUDE_AND_PRUNE = Evaluation.INCLUDE_AND_PRUNE
EXCLUDE_AND_CONTINUE = Evaluation.EXCLUDE_AND_CONTINUE
EXCLUDE_AND_PRUNE = Evaluation.EXCLUDE_AND_PRUNE


class DynamicEvaluator(implements(Evaluator)):
    def __init__(self, eval_method):
        self._eval_method = eval_method

    def evaluate(self, path):
        return self._eval_method(path)


class Traversal(extends(Traversal)):
    pass


class TraversalDescription(extends(TraversalDescription)):

    _relationships = TraversalDescription.relationships

    def relationships(self, rel, direction=None):
        if direction:
            return self._relationships(rel_type(rel))
        else:
            return self._relationships(rel_type(rel), direction)

#
# Pythonification of the traversal API
#

# This is a messy hack, but will only have to be here until
# 1.9, when the traversal support in python is dropped. After that,
# though, the WrappedPath class still needs something like this for
# cypher support.
