import os
import vtk
import slicer
from gltf2usd import convert_to_usd

def export_usd():
    # Set utils path 
    project_dir = slicer.mrmlScene.GetRootDirectory().strip("/")

    # Set export files.
    # file name is the name of your project directory by default.
    project_name = os.path.basename(project_dir)
    gltf_file_path = "{}/export/{}.gltf".format(project_dir, project_name)
    usd_file_path = gltf_file_path.replace(".gltf", ".usda")

    # Export gltf
    exporter = vtk.vtkGLTFExporter()
    exporter.SetRenderWindow(slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow())
    exporter.SetFileName(gltf_file_path)
    exporter.Write()

    # Convert to USD
    try: 
        convert_to_usd(gltf_file_path, usd_file_path, 24, 1)
        print("USD is successfully Exported: {}".format(usd_file_path))
    except Exception as e:
        print("Something went wrong!, {}".format(e))
