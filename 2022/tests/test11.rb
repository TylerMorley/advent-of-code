require 'test/unit'
require 'code/day11'

class Part1 < Test::Unit::TestCase
  def test_get_input
    day11 = Day11.new

    input = day11.get_input('inputs/testinput11.txt')[3]
    expected = ['Monkey 3:', 
                'Starting items: 74', 
                'Operation: new = old + 3', 
                'Test: divisible by 17', 
                'If true: throw to monkey 0', 
                'If false: throw to monkey 1'
               ]

    assert_equal expected, input
  end

  def test_make_monkey
    day11 = Day11.new

    input = ['Monkey 3:', 
             'Starting items: 74, 24', 
             'Operation: new = old + 3', 
             'Test: divisible by 17', 
             'If true: throw to monkey 0', 
             'If false: throw to monkey 1'
            ]

    output = day11.make_monkey(input, 1)

    assert_equal(3, output.id)
    assert_equal([74, 24], output.items)
    assert_equal(['old', '+', '3'], output.operation)
    assert_equal(17, output.test)
    assert_equal(0, output.if_true)
    assert_equal(1, output.if_false)
  end

  def test_execute_round
    monkey0 = Monkey.new(0, [79, 98], 'old * 19', 23, 2, 3, 1)
    monkey1 = Monkey.new(1, [54, 65, 75, 74], 'old + 6', 19, 2, 0, 1)
    monkey2 = Monkey.new(2, [79, 60, 97], 'old * old', 13, 1, 3, 1)
    monkey3 = Monkey.new(3, [74], 'old + 3', 17, 0, 1, 1)
    monkies = [monkey0, monkey1, monkey2, monkey3]
    day11 = Day11.new
    
    day11.execute_round(monkies)

    assert_equal [20, 23, 27, 26], monkey0.items
    assert_equal [2080, 25, 167, 207, 401, 1046], monkey1.items
    assert_equal Array.new, monkey2.items
    assert_equal Array.new, monkey3.items
  end

  def test_find_active_monkey
    monkey0 = Monkey.new(0, [79, 98], 'old * 19', 23, 2, 3, 1)
    monkey1 = Monkey.new(1, [54, 65, 75, 74], 'old + 6', 19, 2, 0, 1)
    monkey2 = Monkey.new(2, [79, 60, 97], 'old * old', 13, 1, 3, 1)
    monkey3 = Monkey.new(3, [74], 'old + 3', 17, 0, 1, 1)
    monkies = [monkey0, monkey1, monkey2, monkey3]
    day11 = Day11.new
    activities = Array.new
    
    monkey_business = day11.find_active_monkey(monkies, 20)

    expected = 10605
    assert_equal expected, monkey_business
  end
end
class TestMonkey < Test::Unit::TestCase
  def test_create
    id = 3
    items = [74]
    test = 17
    operation =  'old + 3'
    if_true = 0
    if_false = 1
    
    output = Monkey.new(id, items, operation, test, if_true, if_false, 1)

    assert_equal(3, output.id)
    assert_equal([74], output.items)
    assert_equal(['old', '+', '3'], output.operation)
    assert_equal(17, output.test)
    assert_equal(0, output.if_true)
    assert_equal(1, output.if_false)
  end

  def test_inspect_item
    items = [74]
    operation = 'old + 3'
    monkey = Monkey.new(0, items, operation, 1, 0, 0, 1)
    
    worry_level = monkey.inspect_item(74)
    expected = 25
    assert_equal expected, worry_level
  end

  def test_test_item
    monkey0 = Monkey.new(0, [25], String.new, 17, 0, 1, 1)
    worry_level = 25

    destination = monkey0.test_item(25)

    expected = 1
    assert_equal expected, destination
  end

  def test_take_turn
    monkey0 = Monkey.new(0, [74], 'old + 3', 17, 0, 1, 1)
    monkey1 = Monkey.new(1, Array.new, String.new, 17, 0, 1, 1)
    monkies = [monkey0, monkey1]

    monkey0.take_turn(monkies)

    assert_equal Array.new, monkey0.items
    assert_equal [25], monkey1.items
    assert_equal 1, monkey0.num_inspected
  end
end
class Part1 < Test::Unit::TestCase
  def test_make_monkey2
    day11 = Day11.new

    input = ['Monkey 3:', 
             'Starting items: 74, 24', 
             'Operation: new = old + 3', 
             'Test: divisible by 17', 
             'If true: throw to monkey 0', 
             'If false: throw to monkey 1'
            ]

    output = day11.make_monkey(input, 2)

    assert_equal(3, output.id)
    assert_equal([74, 24], output.items)
    assert_equal(['old', '+', '3'], output.operation)
    assert_equal(17, output.test)
    assert_equal(0, output.if_true)
    assert_equal(1, output.if_false)
    assert_equal(2, output.part)
  end

  def test_execute_round2
    monkey0 = Monkey.new(0, [79, 98], 'old * 19', 23, 2, 3, 2)
    monkey1 = Monkey.new(1, [54, 65, 75, 74], 'old + 6', 19, 2, 0, 2)
    monkey2 = Monkey.new(2, [79, 60, 97], 'old * old', 13, 1, 3, 2)
    monkey3 = Monkey.new(3, [74], 'old + 3', 17, 0, 1, 2)
    monkies = [monkey0, monkey1, monkey2, monkey3]
    day11 = Day11.new
    
    day11.execute_round(monkies)

    assert_equal 2, monkey0.num_inspected
    assert_equal 4, monkey1.num_inspected
    assert_equal 3, monkey2.num_inspected
    assert_equal 6, monkey3.num_inspected
  end
  def test_find_active_monkey2
    monkey0 = Monkey.new(0, [79, 98], 'old * 19', 23, 2, 3, 2)
    monkey1 = Monkey.new(1, [54, 65, 75, 74], 'old + 6', 19, 2, 0, 2)
    monkey2 = Monkey.new(2, [79, 60, 97], 'old * old', 13, 1, 3, 2)
    monkey3 = Monkey.new(3, [74], 'old + 3', 17, 0, 1, 2)
    monkies = [monkey0, monkey1, monkey2, monkey3]
    day11 = Day11.new
    activities = Array.new
    
    monkey_business = day11.find_active_monkey(monkies, 20)
    # monkey_business = day11.find_active_monkey(monkies, 1000)

    expected = 10197
    # expected = 27019168
    assert_equal expected, monkey_business
  end
end
