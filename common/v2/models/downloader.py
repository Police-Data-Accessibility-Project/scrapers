import os
import requests
import shutil

from common.v2.utils.logging import LogOwnerMixin

class Downloader(LogOwnerMixin, object):
    def process(self, url, save_dir, local_filename=None, overwrite=False):
        self.debug('downloading "%s" to "%s"', url, save_dir)
        local_filename = local_filename or url.split('?')[0].split('/')[-1]
        if local_filename in ['.', '..']:
            raise ValueError('filename invalid')
        p = os.path.join(save_dir, local_filename)
        if os.path.exists(p) and not overwrite:
            self.info('skipping "%s" because it already exists', local_filename)
        else:
            with requests.get(url, stream=True) as r:
                with open(p, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)
    
    def load_list(self, fn, save_dir, **kwargs):
        with open(fn, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('#') or line.startsiwth(';'):
                    # this line must be a comment
                    continue
                yield self.process(line, save_dir, **kwargs)