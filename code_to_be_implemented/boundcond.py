import numpy as np
from typing import Tuple
from provided_code.dofpos import compute_dofpos


class BoundaryConditions:
    """Apply prescribed displacements to a linear-elastic global system.

    Parameters
    ----------
    pdof : np.ndarray, shape (npdof, 3)
        Prescribed DOFs: ``[node#, direction, value]``. Node and direction
        IDs are 1-based; direction is 1, 2, or 3.
    method : float
        If ``method < 0``, use direct elimination. Otherwise, use the penalty
        method with ``Z = method``.
    nnode : int
        Total number of nodes in the structure.
    """

    def __init__(self, pdof: np.ndarray, method: float, nnode: int) -> None:
        self.pdof = pdof
        self.method = method
        self.nnode = nnode

    def apply(self, Ksys: np.ndarray, Fext: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Apply Dirichlet boundary conditions to the structural system.

        Parameters
        ----------
        Ksys : np.ndarray, shape (ndof, ndof)
            Global stiffness matrix before boundary conditions.
        Fext : np.ndarray, shape (ndof,)
            External force vector before boundary conditions.

        Returns
        -------
        Kcl, Fcl : tuple of np.ndarray
            ``Kcl`` is the stiffness matrix with boundary conditions applied;
            ``Fcl`` is the corresponding force vector.

        A tuple is the standard way to return multiple values in Python.
        Python functions always return a single object; writing
        ``return Kcl, Fcl`` bundles both values into a tuple.
        """
        # TODO: Total number of degrees of freedom of the system.
        ndof = ...

        dofpos = compute_dofpos(self.nnode)

        # TODO: Number of prescribed nodal degrees of freedom.
        ndof_node = ...

        # TODO: Initialize Kcl and Fcl.
        # NumPy arrays are mutable, so use .copy() before modifying incoming
        # arrays; otherwise changes can escape this method's scope.
        Fcl = ...
        Kcl = ...

        if self.method < 0:
            # TODO: Direct elimination method.
            pass
        else:
            # TODO: Penalty method.
            Z = float(self.method)
            pass

        return Kcl, Fcl
