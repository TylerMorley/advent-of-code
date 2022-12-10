require 'test/unit'
require 'code/day09'
require 'set'

class Part1 < Test::Unit::TestCase
  def test_get_input
    day9 = Day09.new

    input = day9.get_input('inputs/testinput09.txt')
    expected = [['R', 4],
                ['U', 4],
                ['L', 3],
                ['D', 1],
                ['R', 4],
                ['D', 1],
                ['L', 5],
                ['R', 2]
               ]

    assert_equal expected, input
  end

  def test_move_head
    day9 = Day09.new

    input = 'R'
    head = [0,0]
    output = day9.move_head(head, input)
    expected = [1,0]
    assert_equal expected, output

    input = 'U'
    head = [0,0]
    output = day9.move_head(head, input)
    expected = [0,1]
    assert_equal expected, output
  end

  def test_move_tail
    day9 = Day09.new

    head = [1,0]
    tail = [0,0]
    output = day9.move_tail(head, tail)
    expected = [0,0]
    assert_equal expected, output

    head = [2,0]
    tail = [0,0]
    output = day9.move_tail(head, tail)
    expected = [1,0]
    assert_equal expected, output

    head = [4,3]
    tail = [4,1]
    output = day9.move_tail(head, tail)
    expected = [4,2]
    assert_equal expected, output

    head = [4,2]
    tail = [3,0]
    output = day9.move_tail(head, tail)
    expected = [4,1]
    assert_equal expected, output

    head = [4,3]
    tail = [2,4]
    output = day9.move_tail(head, tail)
    expected = [3,3]
    assert_equal expected, output
  end
    
  def test_move
    day9 = Day09.new
    input = ['R', 4]
    head = [0,0]
    tail = [0,0]
    knots = [head, tail]
    visited = Set.new

    output = day9.move(knots, input, visited)[0]
    expected = [[4, 0], [3,0]]
    assert_equal expected, output
    
    input = ['U', 4]
    output = day9.move(knots, input, visited)[0]
    expected = [[4, 4], [4,3]]
    assert_equal expected, output
  end

  def test_visited
    day9 = Day09.new
    visited = Set.new
    tail = [0,0]
    visited = day9.visit(visited, tail)
    tail = [1,0]
    visited = day9.visit(visited, tail)
    visited = day9.visit(visited, tail)
    
    output = visited.length
    expected = 2
    assert_equal output, expected
  end

  def test_moves
    day9 = Day09.new
    input = [['R', 4],
             ['U', 4],
             ['L', 3],
             ['D', 1],
             ['R', 4],
             ['D', 1],
             ['L', 5],
             ['R', 2]
            ]
    head = [0,0]
    tail = [0,0]
    knots = [head, tail]

    output = day9.moves(knots, input)
    exp_knots = [[2,2], [1,2]]
    exp_num_visited = 13
    expected = [exp_knots, exp_num_visited]
    assert_equal expected, output
  end
end
class Part2 < Test::Unit::TestCase
  def test_moves
    day9 = Day09.new
    input = [['R', 4],
             ['U', 4],
             ['L', 3],
             ['D', 1],
             ['R', 4],
             ['D', 1],
             ['L', 5],
             ['R', 2]
            ]
    knots = Array.new(10).map{|x| [0,0]}

    output = day9.moves(knots, input)
    exp_knots = [[2,2], [1,2], [2,2], [3,2], [2,2], [1,1], [0,0], [0,0], [0,0], [0,0]]
    exp_num_visited = 1
    expected = [exp_knots, exp_num_visited]
    assert_equal expected, output

    input2 = [['R', 5],
              ['U', 8],
              ['L', 8],
              ['D', 3],
              ['R', 17],
              ['D', 10],
              ['L', 25],
              ['U', 20]
             ]

    knots = Array.new(10).map{|x| [0,0]}

    output = day9.moves(knots, input2)
    exp_knots = [[-11,15], [-11,14], [-11,13], [-11,12], [-11,11], [-11,10], [-11,9], [-11,8], [-11,7], [-11,6]]
    exp_num_visited = 36
    expected = [exp_knots, exp_num_visited]
    assert_equal expected, output
  end

  def test_move
    day9 = Day09.new
    input = ['R', 4]
    knots = Array.new(10).map{|x| [0,0]}
    visited = Set.new

    output = day9.move(knots, input, visited)[0]
    expected = [[4, 0], [3,0], [2,0], [1,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    assert_equal expected, output
    
    input = ['U', 4]
    output = day9.move(knots, input, visited)[0]
    expected = [[4, 4], [4,3], [4,2], [3,2], [2,2], [1,1], [0,0], [0,0], [0,0], [0,0]]
    assert_equal expected, output
  end
end
