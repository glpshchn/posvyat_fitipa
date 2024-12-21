import circle
import square
import triangle

FIGS = {
    'circle': {'module': circle, 'params': 1},
    'square': {'module': square, 'params': 1},
    'triangle': {'module': triangle, 'params': 3}
}

FUNCS = ['perimeter', 'area']


def calc(fig, func, size):
    if fig not in FIGS:
        raise ValueError(
            f"Figure '{fig}' is not available. Available figures: "
            f"{list(FIGS.keys())}"
        )
    if func not in FUNCS:
        raise ValueError(
            f"Function '{func}' is not available. Available functions: {FUNCS}"
        )

    module = FIGS[fig]['module']
    func_to_call = getattr(module, func)

    expected_params = FIGS[fig]['params']
    if len(size) != expected_params:
        raise ValueError(
            f"For figure '{fig}', {expected_params} parameter(s) are required, "
            f"but {len(size)} were provided."
        )

    result = func_to_call(*size)
    print(
        f'{func.capitalize()} of {fig} with size(s) {size} is {result}'
    )
    return result
