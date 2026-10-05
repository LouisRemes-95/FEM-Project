import numpy as np
from .elements import ElementType, Tetra4Element
from provided_code.dofpos import compute_dofpos


class Assembler:
    """Assemble a global stiffness matrix from the mesh element table.

    Parameters
    ----------
    node : np.ndarray, shape (nnode, 3)
        Nodal coordinates of the structure.
    elem : np.ndarray, shape (nelem, 2 + nen)
        Element table: ``[type#, material#, node1, node2, ...]``.
    eltp : dict
        Maps type IDs to element names, for example ``{1: "tetra4"}``.
    mater : np.ndarray, shape (nmat, p)
        Material-property table, addressed by 1-based material IDs.

    Notes
    -----
    Element node IDs and material IDs are 1-based (MATLAB style). Convert
    them to 0-based indices before accessing NumPy arrays. Currently the only
    implemented element type is ``tetra4``.
    """

    def __init__(self, node: np.ndarray, elem: np.ndarray, eltp: dict,
                 mater: np.ndarray) -> None:
        self.node = node
        self.elem = elem
        self.eltp = eltp
        self.mater = mater

    def assemble(self) -> np.ndarray:
        """Return the structural stiffness matrix ``Ksys``.

        ``Ksys`` has shape ``(ndof, ndof)``, where ``ndof = 3 * nnode``.
        For efficient large-scale storage, one would use ``scipy.sparse``;
        dense NumPy storage is sufficient for this project.
        """
        # TODO: Number of elements in the structure.
        nelem = ...

        # TODO: Total number of nodes and degrees of freedom.
        nnode = ...
        ndof = ...

        # TODO: Initialize Ksys full of zeros.
        Ksys = ...

        # This helper may be computed once and reused in the element loop.
        dofpos = compute_dofpos(nnode)

        for e in range(nelem):
            type_id = int(self.elem[e, 0])
            try:
                eltpe = ElementType(self.eltp[type_id])
            except (KeyError, ValueError) as exc:
                raise NotImplementedError(
                    f"Element type '{self.eltp.get(type_id, type_id)}' not implemented."
                ) from exc

            match eltpe:
                case ElementType.TETRA4:
                    # TODO: Read 1-based node/material IDs, convert them to
                    # 0-based indices, and construct Tetra4Element(nodee, matere).
                    #
                    # TODO: Obtain Ke = element.stiffness().
                    #
                    # TODO: Find the element's 12 global DOF positions with
                    # dofpos and add Ke to Ksys at those positions.
                    #
                    # !!! Python is a 0-based language !!!
                    pass
                case _:
                    raise NotImplementedError(f"Element type '{eltpe.value}' not implemented.")

        return Ksys
