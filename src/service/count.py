import logging
import time


def do_sizing(num_of_vectors, dim, data_type, index_type, single_deploy, num_of_cluster):
    if dim > 16384 or dim <= 0:
        return "Waring: The dimensions' reference value is (0,16384]."
    if num_of_vectors <=0:
        return "Waring: The num of vectors must above 0."
    if not num_of_cluster:
        num_of_cluster = 0
    if not single_deploy:
        if num_of_cluster <=0:
            return "Waring: The num of cluster must above 0."

    print('\n', num_of_vectors, dim, data_type, index_type, single_deploy, num_of_cluster)

    try:
        size = num_of_vectors*dim*4/1024
        size_status = 1
        status = 'KB'
        while(size_status<3 and size>4096):
            size = size/1024
            status = 'MB'
            size_status += 1
            print(size, status, size_status)
        if size_status == 3:
            status = 'GB'

        if data_type == 'float':
            if index_type == 'IVFSQ8' or index_type == 'IVFSQ8H':
                disk_size = int(size*1.3)+1
                ram_size = int(size*0.3)+1
            else:
                disk_size = int(size*2)+1
                ram_size = int(size)+1
        elif data_type == 'bytes':
            disk_size = int(size/32*2)+1
            ram_size = int(size/32)+1
        if not single_deploy:
            ram_size = int(ram_size+4*num_of_cluster)

        return str(disk_size)+status,str(ram_size)+status

    except Exception as e:
        logging.error(e)
        return "Error with {}".format(e)