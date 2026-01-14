const vscode = require("vscode");
const { exec } = require("child_process");

function activate(context) {
  let disposable = vscode.commands.registerCommand(
    "kaynat.run",
    function () {
      const editor = vscode.window.activeTextEditor;

      if (!editor) {
        vscode.window.showErrorMessage("لا يوجد ملف مفتوح");
        return;
      }

      const filePath = editor.document.fileName;

      exec(`python compiler/main.py "${filePath}"`, (error, stdout, stderr) => {
        if (error) {
          vscode.window.showErrorMessage(stderr);
          return;
        }

        vscode.window.showInformationMessage(stdout);
      });
    }
  );

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
