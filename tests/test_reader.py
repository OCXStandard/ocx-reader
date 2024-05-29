#  Copyright (c) 2024. #  OCX Consortium https://3docx.org. See the LICENSE

from tests.conftest import MODEL1, MODEL8, MODEL6, SCHEMA_VERSION

from ocx_reader.reader.reader import OcxReader


class TestReader:
    def test_read_header(self, shared_datadir):
        model = shared_datadir / MODEL1
        reader = OcxReader(str(model))
        header = reader.read_header().pop()
        assert header.documentation == 'OCX Export'

    def test_read_unit_set(self, shared_datadir):
        model = shared_datadir / MODEL1
        reader = OcxReader(str(model))
        unit_set = reader.read_unit_set().pop()
        assert unit_set.unit.pop().id == 'UkN-M'

    def test_read_principal_particulars(self, shared_datadir):
        model = shared_datadir / MODEL1
        reader = OcxReader(str(model))
        ship_data = reader.read_principal_particulars().pop()
        assert ship_data.lpp.numericvalue == 10.0

    def test_read_pillars(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        pillars = reader.read_pillars()
        assert len(pillars) == 2

    def test_read_brackets(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        brackets = reader.read_brackets()
        assert len(brackets) == 112

    def test_read_plates(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        plates = reader.read_plates()
        assert len(plates) == 63

    def test_read_stiffeners(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        stiffeners = reader.read_stiffeners()
        assert len(stiffeners) == 54

    def test_read_panels(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        panels = reader.read_panels()
        assert len(panels) == 35

    def test_read_material_catalogue(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        catalogue = reader.read_material_catalogue().pop()
        print(catalogue)
        assert len(catalogue.material) == 1

    def test_section_catalogue(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        catalogue = reader.read_section_catalogue().pop()
        assert len(catalogue.bar_section) == 3

    def test_hole_shape_catalogue(self, shared_datadir):
        model = shared_datadir / MODEL6
        reader = OcxReader(str(model))
        catalogue = reader.read_hole_shape_catalogue().pop()
        assert len(catalogue.hole2_d) == 1

    def test_x_ref_planes(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        ref_plane = reader.read_x_ref_planes().pop()
        assert len(ref_plane.ref_plane) == 12

    def test_y_ref_planes(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        ref_plane = reader.read_y_ref_planes().pop()
        assert len(ref_plane.ref_plane) == 21

    def test_z_ref_planes(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        ref_plane = reader.read_z_ref_planes().pop()
        assert len(ref_plane.ref_plane) == 18

    def test_read_reference_surfaces(self, shared_datadir):
        model = shared_datadir / MODEL8
        reader = OcxReader(str(model))
        ref_surf = reader.read_reference_surfaces().pop()
        print (ref_surf)
        assert ref_surf.plane3_d.pop().id == 'nplcid13'

    def test_read_root_xml(self, shared_datadir):
        model = shared_datadir / MODEL1
        reader = OcxReader(str(model))
        root = reader.read_ocx_root()
        assert root.header.author == 'MJ'
