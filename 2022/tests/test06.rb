require 'test/unit'
require 'code/day06'

class Part1 < Test::Unit::TestCase
  def test_get_assignments
    day6 = Day06.new

    datastream = day6.get_input('inputs/testinput06.txt')
    expected = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

    assert_equal expected, datastream
  end

  def test_get_sop_marker
    day6 = Day06.new
    distinct_chars = 4

    input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    expected = 7
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    expected = 5
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'nppdvjthqldpwncqszvftbrmjlhg'
    expected = 6
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprs'
    expected = 10
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    expected = 11
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker
  end
end
class Part2 < Test::Unit::TestCase
  def test_get_sop_marker2
    day6 = Day06.new
    distinct_chars = 14

    input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
    expected = 19
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'bvwbjplbgvbhsrlpgdmjqwftvncz'
    expected = 23
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'nppdvjthqldpwncqszvftbrmjlhg'
    expected = 23
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprs'
    expected = 29
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker

    input = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
    expected = 26
    sop_marker = day6.get_sop_marker(input, distinct_chars)
    assert_equal expected, sop_marker
  end
end
