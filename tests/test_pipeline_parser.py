from basetestcase import BaseTestCase
from gitlabcidocs.pipelineparser import Variable, Rule
import gitlabcidocs.errors as errors


class RuleTestCase(BaseTestCase):

    def test_is_mutable(self):
        rules = [r for source in ['web', 'pipeline', 'trigger', 'api'] for r in [
            f'$CI_PIPELINE_SOURCE == \'{source}\'',
            f'$CI_PIPELINE_SOURCE == "{source}"',
            f'$CI_PIPELINE_SOURCE == {source}'
        ]]
        rules += [f'$CI_COMMIT_BRANCH == "main" && {r}' for r in rules]
        rules += [f'{r} || $CI_COMMIT_BRANCH == "main"' for r in rules]
        for r in rules:
            self.assertTrue(Rule({'if': r}).is_mutable)


class VriableTestCase(BaseTestCase):

    def test_parse_empty_comment(self):
        for comment in ['', '  ', '#', '#  ']:
            v = Variable('env', 'dev', comment=comment)
            self.assertEqual('env', v.name)
            self.assertEqual('dev', v.value)
            self.assertEqual(False, v.required)
            self.assertEqual(True, v.optional)
            self.assertEqual([], v.choices)
            self.assertEqual('', v.typename)

    def test_parse_comment__choices(self):
        comments = [
            ('# dev', ['dev']),
            ('#  dev|test', ['dev', 'test']),
            ('#dev|dev', ['dev']),
            ('# dev|test|prod', ['dev', 'test', 'prod'])
        ]
        for comment, choices in comments:
            v = Variable('env', 'dev', comment)
            self.assertEqual(False, v.required)
            self.assertEqual(True , v.optional)
            self.assertEqual(sorted(choices), sorted(v.choices))
            self.assertEqual(None, v.typename)

    def test_parse_comment__choices_special_chars(self):
        for char in '-_.':
            v = Variable('env', 'dev', comment=f'# dev{char}dev')
            self.assertEqual(False, v.required)
            self.assertEqual(True , v.optional)
            self.assertEqual([f'dev{char}dev'], v.choices)
            self.assertEqual(None, v.typename)

    def test_parse_comment__choices_invalid_chars(self):
        for char in '*/";,:+':
            with self.assertRaises(errors.BadVariableCommentFormatError):
                Variable('env', 'dev', comment=f'dev{char}dev')

    def test_parse_comment__typename(self):
        comments = [
            ('#:str', 'str'),
            ('#   :blabli', 'blabli')
        ]
        for comment, typename in comments:
            v = Variable('env', 'dev', comment)
            self.assertEqual(False, v.required)
            self.assertEqual(True, v.optional)
            self.assertEqual([], v.choices)
            self.assertEqual(typename, v.typename)

    def test_parse_comment__typename_invalid_chars(self):
        comments = [f'# :dev{char}dev' for char in '*/";,:-_+']
        for c in comments + ['::str', ':str|dev']:
            with self.assertRaises(errors.BadVariableCommentFormatError):
                Variable('env', 'dev', c)


    def test_parse_comment__required_typename(self):
        comments = [
            ('# required :str', 'str'),
            ('#required :blabli','blabli'),
            ('#  required:str','str')
        ]
        for comment, typename in comments:
            v = Variable('env', 'dev', comment)
            self.assertEqual(True, v.required)
            self.assertEqual(False, v.optional)
            self.assertEqual([], v.choices)
            self.assertEqual(typename, v.typename)

    def test_parse_comment__required_choices(self):
        comments = [
            ('# required dev', ['dev']),
            ('# required dev|test', ['dev', 'test']),
            ('# required dev|dev', ['dev']),
            ('# required dev|test|prod', ['dev', 'test', 'prod'])
        ]
        for comment, choices in comments:
            v = Variable('env', 'dev', comment)
            self.assertEqual(True, v.required)
            self.assertEqual(False, v.optional)
            self.assertEqual(sorted(choices), sorted(v.choices))
            self.assertEqual(None, v.typename)

    def test_parse_comment__required(self):
        v = Variable('env', 'dev', comment='# required')
        self.assertEqual(True, v.required)
        self.assertEqual(False, v.optional)
        self.assertEqual([], v.choices)
        self.assertEqual(None, v.typename)