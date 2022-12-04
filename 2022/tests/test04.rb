require 'test/unit'
require 'code/day04'

class Part1 < Test::Unit::TestCase
  def test_get_assignments
    day4 = Day04.new

    assignments = day4.get_assignments('inputs/testinput04.txt')
    expected = [[[2,4],[6,8]],
                [[2,3],[4,5]],
                [[5,7],[7,9]],
                [[2,8],[3,7]],
                [[6,6],[4,6]],
                [[2,6],[4,8]]
               ]

    assert_equal expected, assignments
  end
  
  def test_check_pair
    day4 = Day04.new

    pair = [[2,4],[6,8]]
    has_containment = day4.check_pair(pair)
    expected = false
    assert_equal expected, has_containment

    pair2 = [[2,8],[3,7]]
    has_containment = day4.check_pair(pair2)
    expected = true
    assert_equal expected, has_containment

    pair3 = [[6,6],[4,6]]
    has_containment = day4.check_pair(pair3)
    expected = true
    assert_equal expected, has_containment
  end

  def test_count_containments
    day4 = Day04.new
    assignments = [[[2,4],[6,8]],
                   [[2,3],[4,5]],
                   [[5,7],[7,9]],
                   [[2,8],[3,7]],
                   [[6,6],[4,6]],
                   [[2,6],[4,8]]
                  ]
    
    count = day4.count_containments(assignments)
    expected = 2
    assert_equal expected, count
  end
end
