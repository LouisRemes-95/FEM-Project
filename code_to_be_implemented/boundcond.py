import numpy as np
from typing import Tuple

def boundcond(pdof: np.ndarray,
              Ksys: np.ndarray,
              Fext: np.ndarray,
              method: float,
              nnode: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Apply Dirichlet boundary conditions to the structural system.

    Parameters
    ----------
    pdof : (npdof, 3) array
        Prescribed DOFs: [node#, dir, value] with 1-based node# and dir ∈ {1,2,3}.
    Ksys : (ndof, ndof) array
        Global stiffness matrix before BCs (dense).
    Fext : (ndof,) array
        External force vector before BCs.
    method : float
        If method < 0  → direct elimination method.
        If method >= 0 → penalty method with Z = method.
    nnode : int
        Total number of nodes in the structure.

    Returns
    -------
    Kcl, Fcl : tuple of np.ndarray
        - Kcl : Stiffness matrix with BCs applied (same shape as Ksys)
        - Fcl : Force vector with BCs applied (same shape as Fext)
    """

    # TODO: Total number of degrees of freedom of the system
    ndof = 

    # Build dofpos: shape (nnode, 3)
    dofpos = np.vstack([
        np.arange(0, ndof, 3),
        np.arange(1, ndof, 3),
        np.arange(2, ndof, 3),
    ]).T

    # TODO: Number of nodal degrees of freedom
    ndof_node = 

    # TODO: Initialize Kcl and Fcl 
    # !!! Numpy arrays are mutable, so can be modified outside of the function scope. See .copy()
    Fcl = 
    Kcl = 

    if method < 0:
        # TODO: Direct method
    else:
        # TODO: Penalty method
        Z = float(method)

    return Kcl, Fcl
