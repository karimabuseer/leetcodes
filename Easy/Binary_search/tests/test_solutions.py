import pytest
from Binary_search.solutions import SolutionOOfN, SolutionOLogN

@pytest.mark.parametrize(
    ["nums", "target", "expected_return"],
    [
        # Case 1: Target is in nums list
        (
            [-1,0,3,5,9,12],
            9,
            4
        ),
        # Case 2: The target is not in the nums list
        (
            [-1,0,3,5,9,12],
            2,
            -1
        )
    ]
)
def test_o_of_n_solution(nums, target, expected_return):
    solution = SolutionOOfN()
    assert solution.search(nums, target) == expected_return

@pytest.mark.parametrize(
    ["nums", "target", "expected_return"],
    [
        # Case 1: Target is in nums list
        (
            [-1,0,3,5,9,12],
            9,
            4
        ),
        # Case 2: The target is not in the nums list
        (
            [-1,0,3,5,9,12],
            2,
            -1
        )
    ]
)
def test_o_of_logn_solution(nums, target, expected_return):
    solution = SolutionOLogN()
    assert solution.search(nums, target) == expected_return
