import unittest

import numpy as np
from PIL import Image

from torchcam import utils


class UtilsTester(unittest.TestCase):
    def test_overlay_mask(self):

        img = Image.fromarray(np.zeros((4, 4, 3)).astype(np.uint8))
        mask = Image.fromarray(255 * np.ones((4, 4)).astype(np.uint8))

        overlayed = utils.overlay_mask(img, mask, alpha=0.7)

        # Check object type
        self.assertIsInstance(overlayed, Image.Image)
        # Verify value
        self.assertTrue(np.all(np.asarray(overlayed)[..., 0] == 0))
        self.assertTrue(np.all(np.asarray(overlayed)[..., 1] == 0))
        self.assertTrue(np.all(np.asarray(overlayed)[..., 2] == 39))


if __name__ == '__main__':
    unittest.main()
