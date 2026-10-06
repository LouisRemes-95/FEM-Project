from enum import Enum
import numpy as np

class ElementType(Enum):
    TETRA4 = "tetra4"

# ============================================================
# Object-oriented student API
# ============================================================

class Tetra4Element:
    """A four-node, three-dimensional linear-elastic tetrahedral element.

    Parameters
    ----------
    nodee : np.ndarray, shape (4, 3)
        Element nodal coordinates. Each row is ``[x, y, z]``.
    matere : np.ndarray
        Material properties ``[E, nu]``.
    """

    def __init__(self, nodee: np.ndarray, matere: np.ndarray) -> None:
        self.nodee = np.asarray(nodee, dtype=float)
        self.matere = np.asarray(matere, dtype=float)

    # Core helpers
    # I created these for ease of implementation, but you are not required to
    # use helper methods if you prefer a different organisation.
    def coordinate_transform(self) -> np.ndarray:
        """Build the 4-by-4 coordinate transformation matrix.

        Returns
        -------
        Ct : np.ndarray, shape (4, 4)
            ``[[1, 1, 1, 1], [x1, x2, x3, x4],
              [y1, y2, y3, y4], [z1, z2, z3, z4]]``.
        """
        # TODO: Build Ct from self.nodee.
        raise NotImplementedError("TODO: implement coordinate_transform")

    def volume(self) -> float:
        """Compute the volume of a 4-node tetrahedron.

        Returns
        -------
        Ve : float
            Element volume.
        """
        # TODO: Compute Ve from self.nodee.
        raise NotImplementedError("TODO: implement volume")

    def b_matrix(self) -> np.ndarray:
        """Build the 6-by-12 strain-displacement matrix.

        Returns
        -------
        B : np.ndarray, shape (6, 12)
            Strain-displacement matrix such that ``strain = B @ u_e``.
        """
        # TODO: Compute B from self.nodee.
        raise NotImplementedError("TODO: implement b_matrix")

    def hooke_matrix(self) -> np.ndarray:
        """Build the 6-by-6 Hooke matrix for 3D isotropic elasticity.

        Returns
        -------
        H : np.ndarray, shape (6, 6)
            Constitutive matrix.
        """
        # TODO: Compute H from self.matere = [E, nu].
        raise NotImplementedError("TODO: implement hooke_matrix")

    def stiffness(self) -> np.ndarray:
        """Compute the stiffness matrix for this 4-node tetrahedron.

        Returns
        -------
        Ke : np.ndarray, shape (12, 12)
            Element stiffness matrix.
        """
        # TODO: Compute the stiffness matrix of the finite element.
        raise NotImplementedError("TODO: implement stiffness")

    def strain_stress(self, ue: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        """Compute constant strain and stress for this 4-node tetrahedron.

        Parameters
        ----------
        ue : np.ndarray, shape (12,)
            Element displacement vector, ordered as
            ``[u1x, u1y, u1z, ..., u4x, u4y, u4z]``.

        Returns
        -------
        strain : np.ndarray, shape (6,)
            Engineering strain vector.
        stress : np.ndarray, shape (6,)
            Cauchy stress vector.

        A tuple is the standard way to return multiple values in Python.
        Python functions always return a single object; writing
        ``return strain, stress`` bundles both values into a tuple.
        """
        # TODO: Post-process ue to compute and return (strain, stress).
        raise NotImplementedError("TODO: implement strain_stress")
