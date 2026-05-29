import pytest
from tests.support.builders.double_battle_builder import DoubleBattleBuilder
from tests.support.utils.orders import (
    create_double_battle_order_with_first,
    create_double_battle_order_with_second,
    create_tera_order,
)

from shiny_venipede.strategies.tera.first_turn_tera_strategy import (
    FirstTurnTeraStrategy,
)


def test_non_first_turn_returns_none(
    first_turn_tera_strategy: FirstTurnTeraStrategy,
):
    orders = [create_double_battle_order_with_first(create_tera_order())]

    battle = DoubleBattleBuilder().with_turn(2).build()

    result = first_turn_tera_strategy.filter_orders(battle, orders)

    assert result is None


def test_tera_solt_0_filters_first_order_only(
    first_turn_tera_strategy: FirstTurnTeraStrategy,
):
    battle = DoubleBattleBuilder().with_turn(1).build()

    valid_double_order = create_double_battle_order_with_first(create_tera_order())

    invalid_double_order = create_double_battle_order_with_first(
        create_tera_order(False)
    )

    double_battle_orders = [valid_double_order, invalid_double_order]

    result = first_turn_tera_strategy.filter_orders(battle, double_battle_orders)

    assert result == [valid_double_order]


@pytest.mark.parametrize(
    "first_turn_tera_strategy",
    [1],
    indirect=True,
)
def test_tera_solt_1_filters_first_order_only(
    first_turn_tera_strategy: FirstTurnTeraStrategy,
):
    battle = DoubleBattleBuilder().with_turn(1).build()

    valid_double_order = create_double_battle_order_with_second(create_tera_order())

    invalid_double_order = create_double_battle_order_with_second(
        create_tera_order(False)
    )

    double_battle_orders = [valid_double_order, invalid_double_order]

    result = first_turn_tera_strategy.filter_orders(battle, double_battle_orders)

    assert result == [valid_double_order]


def test_no_valid_order_returns_None(
    first_turn_tera_strategy: FirstTurnTeraStrategy,
):
    battle = DoubleBattleBuilder().with_turn(1).build()

    invalid_double_order = create_double_battle_order_with_second(
        create_tera_order(False)
    )

    double_battle_orders = [invalid_double_order]

    result = first_turn_tera_strategy.filter_orders(battle, double_battle_orders)

    assert result is None


def test_multiple_valid_orders_are_preserved(
    first_turn_tera_strategy: FirstTurnTeraStrategy,
):
    battle = DoubleBattleBuilder().with_turn(1).build()

    valid_double_order_1 = create_double_battle_order_with_first(create_tera_order())
    valid_double_order_2 = create_double_battle_order_with_first(create_tera_order())
    invalid_double_order = create_double_battle_order_with_first(
        create_tera_order(False)
    )

    double_battle_orders = [
        valid_double_order_1,
        valid_double_order_2,
        invalid_double_order,
    ]

    result = first_turn_tera_strategy.filter_orders(battle, double_battle_orders)

    assert result == [valid_double_order_1, valid_double_order_2]
