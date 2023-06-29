"""
python path_to_dir/compare_yaml.py path_to_dir/file1.yaml path_to_dir/file2.yaml
"""
import argparse
import yaml
import dictdiffer

parser = argparse.ArgumentParser(description='Convert two yaml files to dict and compare equality. Allows comparison of differently ordered keys.')
parser.add_argument('file_paths', type=str, nargs=1,
                    help='Full paths to yaml documents')
args = parser.parse_args()

# print(f"File Path: {args.file_paths[0]}")
# print(f"File Path Target: {args.file_paths[1]}")

with open(args.file_paths[0],'r') as rdr:
    data1=rdr.read()


data2_dict = yaml.load(data1,Loader=yaml.FullLoader)

# if 'annotations' in data2_dict['metadata']:
#     del data2_dict['metadata']['annotations']
#
# if 'creationTimestamp' in data2_dict['metadata']:
#     del data2_dict['metadata']['creationTimestamp']
#
# if 'generation' in data2_dict['metadata']:
#     del data2_dict['metadata']['generation']
#
# if 'resourceVersion' in data2_dict['metadata']:
#     del data2_dict['metadata']['resourceVersion']
#
# if 'uid' in data2_dict['metadata']:
#     del data2_dict['metadata']['uid']
#
# if 'progressDeadlineSeconds' in data2_dict['spec']:
#     del data2_dict['spec']['progressDeadlineSeconds']
#
# if 'revisionHistoryLimit' in data2_dict['spec']:
#     del data2_dict['spec']['revisionHistoryLimit']
#
# if 'strategy' in data2_dict['spec']:
#     del data2_dict['spec']['strategy']
#
# if 'annotations' in data2_dict['spec']['template']['metadata']:
#     del data2_dict['spec']['template']['metadata']['annotations']
#
# if 'creationTimestamp' in data2_dict['spec']['template']['metadata']:
#     del data2_dict['spec']['template']['metadata']['creationTimestamp']
#
# if 'terminationMessagePath' in data2_dict['spec']['template']['spec']['containers'][0]:
#     del data2_dict['spec']['template']['spec']['containers'][0]['terminationMessagePath']
# if 'terminationMessagePolicy' in data2_dict['spec']['template']['spec']['containers'][0]:
#     del data2_dict['spec']['template']['spec']['containers'][0]['terminationMessagePolicy']
#
# if 'dnsPolicy' in data2_dict['spec']['template']['spec']:
#     del data2_dict['spec']['template']['spec']['dnsPolicy']
#
# if 'restartPolicy' in data2_dict['spec']['template']['spec']:
#     del data2_dict['spec']['template']['spec']['restartPolicy']
#
# if 'schedulerName' in data2_dict['spec']['template']['spec']:
#     del data2_dict['spec']['template']['spec']['schedulerName']
#
# if 'terminationGracePeriodSeconds' in data2_dict['spec']['template']['spec']:
#     del data2_dict['spec']['template']['spec']['terminationGracePeriodSeconds']
#
# if 'status' in data2_dict:
#     del data2_dict['status']
#
# if 'scheme' in data2_dict['spec']['template']['spec']['containers'][0]['livenessProbe']['httpGet']:
#     del data2_dict['spec']['template']['spec']['containers'][0]['livenessProbe']['httpGet']['scheme']
#
# if 'scheme' in data2_dict['spec']['template']['spec']['containers'][0]['readinessProbe']['httpGet']:
#     del data2_dict['spec']['template']['spec']['containers'][0]['readinessProbe']['httpGet']['scheme']
#
# if 'protocol' in data2_dict['spec']['template']['spec']['containers'][0]['ports'][0]:
#     del data2_dict['spec']['template']['spec']['containers'][0]['ports'][0]['protocol']
#
# if 'imagePullPolicy' in data2_dict['spec']['template']['spec']['containers'][0]:
#     del data2_dict['spec']['template']['spec']['containers'][0]['imagePullPolicy']
#
# if 'securityContext' in data2_dict['spec']['template']['spec']:
#     del data2_dict['spec']['template']['spec']['securityContext']

# print(type(data2_dict))

# if data1_dict == data2_dict:
#     print("No difference detected")
# else:
#     print("Differences detected:")
#     for diff in list(dictdiffer.diff(data1_dict, data2_dict)):
#         print(type(diff))

# result = yaml.dump(diff, allow_unicode=True, default_flow_style=False)
# file=open(args.file_paths[1],"w")
# yaml.dump(data2_dict, file)
# file.close()
print(data2_dict['spec']['template']['spec']['containers'][0]['envFrom'][0]['configMapRef']['name'])