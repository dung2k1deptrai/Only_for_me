# import ruamel.yaml
#
# file_name = 'test.yaml'
# config, ind, bsi = ruamel.yaml.util.load_yaml_guess_indent(open(file_name))
#
# instances = config['spec']
# instances['template']['spec']['containers'][0]['securityContext']['readOnlyRootFilesystem'] = "true"
# # instances[0]['username'] = 'Username'
# # instances[0]['password'] = 'Password'
#
# yaml = ruamel.yaml.YAML()
# yaml.indent(mapping=ind, sequence=ind, offset=bsi)
# with open('output.yaml', 'w') as fp:
#     yaml.dump(config, fp)

# import yaml
#
# fname = "test.yaml"
#
# stream = open(fname, 'r')
# data = yaml.full_load(stream)
#
# data['spec']['template']['spec']['containers'][0]['securityContext']['readOnlyRootFilesystem'] = True
#
#
# with open(fname, 'w') as yaml_file:
#     yaml_file.write( yaml.dump(data, default_flow_style=False))

# loop through file in folder
import glob

for filepath in glob.iglob('D:\Only_for_me\yaml-diff-tool/*.py'):
    print(filepath)