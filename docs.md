<table>
<tr><th>Trigger</th><th>Variable</th><th>Required</th><th>Type</th><th>Choices</th><th>Default</th></tr>
<tr><td rowspan="3">if: $CI_COMMIT_TAG</td><td>ENV</td><td>No</td><td>-</td><td>prod test dev</td><td>dev</td></tr><tr><td>ACC_ID</td><td>No</td><td>str</td><td>-</td><td>None</td></tr>
<tr><td>MODE</td><td>Yes</td><td>-</td><td>dep art</td><td>bla</td></tr>
<tr><td rowspan="2">if: $CI_PIPELINE_SOURCE == 'push'</td><td>ENV</td><td>Yes</td><td>-</td><td>prod test dev</td><td>stage</td></tr><tr><td>ACC_ID</td><td>Yes</td><td>str</td><td>-</td><td>None</td></tr>
</table>