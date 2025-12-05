# Boilerplate Template

Simple boilerplate test procedure with plug and phase.

## Structure

```
basic/
âââ procedure.yaml              # Test procedure definition
âââ phases/
â   âââ run_test.py            # Test phase implementation
âââ plugs/
    âââ python/
        âââ test_instrument.py # Instrument plug implementation
```

## Usage

1. Copy this template to your project location
2. Modify `procedure.yaml` for your test requirements
3. Implement your test logic in `phases/run_test.py`
4. Customize instrument plug in `plugs/python/test_instrument.py`

## Key Concepts

- **Plugs**: Shared hardware resources with lifecycle management
- **Phases**: Test execution units that run sequentially
- **Workers**: Parallel execution (2 workers = 2 units tested simultaneously)
