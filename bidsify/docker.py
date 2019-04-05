import os
import subprocess
import os.path as op
from datetime import datetime
from .utils import _run_cmd
from .version import __version__


def run_from_docker(cfg_path, directory, out_dir, validate, spinoza):
    """ Runs bidsify from Docker. """

    proj_name = op.basename(op.dirname(directory))
    date = str(datetime.now().strftime("%Y-%m-%d"))
    if spinoza:
        log_file = op.join(op.dirname(op.dirname(out_dir)), 'logs', 'project-%s_stage-bidsify_%s' % (proj_name, date))
    else:
        log_file = op.join(out_dir, 'log')

    uid = str(os.getuid())
    cmd = ['docker', 'run', '--rm',
           '-u', uid + ':' + uid,
           '-v', '%s:/data' % directory,
           '-v', '%s:/config.yml' % cfg_path,
           '-v', '%s:/bids' % out_dir,
           #'-v', '%s:/unallocated' % op.join(out_dir, 'unallocated'),
           'lukassnoek/bidsify:%s' % __version__, 'bidsify', '-c', '/config.yml', '-d', '/data', '-o', '/bids']

    if validate:
        cmd.append('-v')

    if spinoza:
        cmd.append('-s')

    if not op.isdir(out_dir):
        # Need to create dir beforehand, otherwise it's owned by root
        os.makedirs(out_dir)

    print("Writing logfile to %s ..." % log_file)
    print("RUNNING:")
    print(' '.join(cmd))

    fout = open(log_file + '_stdout.txt', 'w')
    ferr = open(log_file + '_stderr.txt', 'w')
    subprocess.run(cmd, stdout=fout, stderr=ferr)
    fout.close()
    ferr.close()
