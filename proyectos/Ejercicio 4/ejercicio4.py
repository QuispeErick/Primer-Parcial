import pandas as pd

relaciones = pd.DataFrame({
    'Persona': ['Abuelo', 'Abuela', 'Abuelo', 'Abuela', 'Padre1', 'Padre2', 'Padre2', 'Padre1', 'Hijo2', 'Hijo1', 'Hijo1', 'Hijo2'],
    'Relacion': ['Padre', 'Madre', 'Padre',    'Madre',  'Padre', 'Padre', 'Tio',      'Tio', 'Primo',   'Primo', 'Hijo', 'Hijo'],
    'Familiar': ['Padre1', 'Padre1', 'Padre2', 'Padre2', 'Hijo1', 'Hijo2', 'Hijo1', 'Hijo2', 'Hijo1', 'Hijo2',  'Padre1', 'Padre2']
})


print(relaciones)