require 'test/unit'
require 'code/day08'

class Part1 < Test::Unit::TestCase
  def test_get_input
    day8 = Day08.new

    input = day8.get_input('inputs/testinput08.txt')
    expected = ['$ cd /', '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d', '$ cd a', '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst', '$ cd e', '$ ls', '584 i', '$ cd ..', '$ cd ..', '$ cd d', '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']

    assert_equal expected, input
  end

  def test_organize
    day7 = Day07.new
    input = ['$ cd /',
             '$ ls', 'dir a', '14848514 b.txt', '8504156 c.dat', 'dir d',
             '$ cd a',
             '$ ls', 'dir e', '29116 f', '2557 g', '62596 h.lst',
             '$ cd e',
             '$ ls', '584 i',
             '$ cd ..',
             '$ cd ..',
             '$ cd d',
             '$ ls', '4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k'
            ]
    expected = [['cd', '/'],
                ['ls', ['dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']],
                ['cd', 'a'],
                ['ls', ['dir e', '29116 f', '2557 g', '62596 h.lst']],
                ['cd', 'e'],
                ['ls', ['584 i']],
                ['cd', '..'],
                ['cd', '..'],
                ['cd', 'd'],
                ['ls', ['4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']]
               ]
    
    organized = day7.organize(input)

    assert_equal expected, organized
  end

end
class TestFsNode < Test::Unit::TestCase
  def test_new
    value = '/'
    root = FsNode.new(value)
    expected = '/'
    assert_equal expected, root.name
  end

  def test_make_tree
    instr = [['cd', '/']]
    day7 = Day07.new
    tree = day7.make_tree(instr)
    expected = '/'

    assert_equal expected, tree.name
  end

  def test_add_nodes
        instr = [['cd', '/'],
             ['ls', ['dir a', '14848514 b.txt', '8504156 c.dat', 'dir d']]#,
             # ['cd', 'a'],
             # ['ls', ['dir e', '29116 f', '2557 g', '62596 h.lst']],
             # ['cd', 'e'],
             # ['ls', ['584 i']],
             # ['cd', '..'],
             # ['cd', '..'],
             # ['cd', 'd'],
             # ['ls', ['4060174 j', '8033020 d.log', '5626152 d.ext', '7214296 k']]
            ]

        day7 = Day07.new
        tree = day7.make_tree(instr)
        expected = 4
        output = tree.children.length
        assert_equal expected, output
  end
end
