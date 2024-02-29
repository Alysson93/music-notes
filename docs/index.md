![logo_projeto](assets/logo.png){width="300", .center}
# Music Notes


## Como usar?

{% include "templates/cards.html" %}

{% include "templates/installation.md" %}

## Escalas

Você pode chamar as escalas via linha de comando. Por exemplo:

```bash
{{ commands.run }} scales f menor
```

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ F │ G  │ Ab  │ Bb │ C │ Db │ Eb  │
└───┴────┴─────┴────┴───┴────┴─────┘
```

Por padão, a escala é A, e a tonalidade é maior.

## Acordes

Você pode chamar os acordes via linha de comando. Por exemplo:

```bash
{{ commands.run }} chords Fm
```

```bash
┏━━━┳━━━━━━┳━━━┓
┃ I ┃ III- ┃ V ┃
┡━━━╇━━━━━━╇━━━┩
│ F │ Ab   │ C │
└───┴──────┴───┘
```

Por padão, a cifra é A


## Campo Harmônico

Você pode chamar o campo harmônico de um tom via linha de comando. Por exemplo:

```bash
{{ commands.run }} harmonic-fields F menor
```

```bash
┏━━━━┳━━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii- ┃ III ┃ iv  ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━━┩
│ Fm │ G°  │ Ab  │ Bbm │ Cm │ Db │ Eb  │
└────┴─────┴─────┴─────┴────┴────┴─────┘
```

Por padão, o tom é A maior