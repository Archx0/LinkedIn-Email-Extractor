<!DOCTYPE html>
<html>

<body>
  <h1>Email Generator</h1>

  <p>Generate emails from names in LinkedIn</p>

  <ol>
    <li>Open LinkedIn and go to the company profile.</li>
    <li>Click on the "People" section.</li>
    <li>Load as many profiles as possible.</li>
    <li>Inspect and copy the HTML element as shown below:</li>
  </ol>
  <img src="img/inspect.png" width="950px">

  <p>Then paste the copied HTML element into the <code>index.html</code> file.</p>

  <p>Next, run the script:</p>

  <pre><code>python3 getEmail.py</code></pre>
  <img src="img/run_script.png" width="950px">

  <p>The script will generate two files: <code>email.txt</code> and <code>name_and_email.txt</code>.</p>
  <img src="img/results.png" width="950px">

  <p>The <code>email.txt</code> file contains a list of the generated email addresses, while the <code>name_and_email.txt</code> file provides a corresponding list of names and their respective email addresses.</p>

  <p>Feel free to modify and enhance the script according to your specific requirements.</p>

  <p><strong>Note:</strong> Ensure that you have the necessary permissions and adhere to LinkedIn's terms and conditions when using this tool. Respect privacy and use the generated emails responsibly.</p>
</body>

</html>
