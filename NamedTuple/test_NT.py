from NamedTuple.NT import Task
from datetime import datetime


class TestNT:
    possible_tasks = ['buy_something', 'do_laundry', 'wash_dishes', 'feed_the_pet', 'pick_up_mail']
    today = datetime.today()
    f_today = today.strftime('%Y-%m-%d')

    def test_defaults(self):
        tsk_1 = Task()
        tsk_2 = Task(None, None, False, None)

        assert tsk_1 == tsk_2

    def test_access(self):
        tsk = Task('buy_something', 'Artur')

        assert tsk.summary == 'buy_something'
        assert tsk.owner == 'Artur'
        assert (tsk.is_done, tsk.date) == (False, None)

    def test_asdict(self):
        tsk = Task('do_laundry', 'Yuri', True, self.f_today)
        tsk_dict = tsk._asdict()
        expected = {'summary': 'do_laundry',
                    'owner': 'Yuri',
                    'is_done': True,
                    'date': self.f_today}

        assert tsk_dict == expected

    def test_replace(self):
        tsk = Task('finish book', 'brian', False)
        tsk_changed = tsk._replace(date=self.f_today, is_done=True)
        tsk_expected = Task('finish book', 'brian', True, self.f_today)

        assert tsk_changed == tsk_expected
