from doltpy.cli import Dolt
from doltpy.cli.write import write_file

dolt = Dolt.clone('dolthub/pdap/datasets')
write_file(dolt,
           '/USA/CA/citrus_college/data/crime_logs/tables/',
           open('data/crime_logs/tables/2020CrimeLog.csv'),
           import_mode('update'))
dolt.push('origin', 'master')
