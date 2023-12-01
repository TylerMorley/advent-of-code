require 'test/unit'
require 'code/day12'

class Part1 < Test::Unit::TestCase

  def setup
    @day12 = Day12.new
    @heightmap = [['S','a','b','q','p','o','n','m'],
                 ['a','b','c','r','y','x','x','l'],
                 ['a','c','c','s','z','E','x','k'],
                 ['a','c','c','t','u','v','w','j'],
                 ['a','b','d','e','f','g','h','i']
                ]
  end
  def test_get_heightmap
    input = @day12.get_heightmap('inputs/testinput12.txt')
    expected = @heightmap

    assert_equal expected, input
  end

  def test_get_possibile_paths
    hmap = @heightmap.map{|row| row.map{|x| x.dup}}
  end
end
