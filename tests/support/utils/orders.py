from poke_env.player import DoubleBattleOrder, SingleBattleOrder
from tests.support.builders.double_battle_order_builder import DoubleBattleOrderBuilder
from tests.support.builders.single_battle_order_builder import SingleBattleOrderBuilder


def create_tera_order(valid: bool = True) -> SingleBattleOrder:
    return SingleBattleOrderBuilder().with_terastallize(valid).build()


def create_double_battle_order_with_first(
    single_order: SingleBattleOrder,
) -> DoubleBattleOrder:
    return DoubleBattleOrderBuilder().with_first_order(single_order).build()


def create_double_battle_order_with_second(
    single_order: SingleBattleOrder,
) -> DoubleBattleOrder:
    return DoubleBattleOrderBuilder().with_second_order(single_order).build()


def create_default_double_battle_order() -> DoubleBattleOrder:
    return DoubleBattleOrderBuilder().build()
