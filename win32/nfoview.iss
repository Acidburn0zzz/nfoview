; -*- conf -*-

[Setup]
AppId=io.otsaloma.nfoview
AppName=NFO Viewer
AppVerName=NFO Viewer 1.19.20160715
AppPublisher=Osmo Salomaa
AppPublisherURL=http://otsaloma.io/nfoview/
DefaultDirName={pf}\NFO Viewer
DefaultGroupName=NFO Viewer
AllowNoIcons=yes
OutputDir=".."
OutputBaseFilename=nfoview-1.19.20160715-win32
Compression=lzma
SolidCompression=yes

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\build\exe.win32-3.4\*"; DestDir: {app}; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{commonprograms}\NFO Viewer"; Filename: "{app}\nfoview.exe"
Name: "{commondesktop}\NFO Viewer"; Filename: "{app}\nfoview.exe"; Tasks: desktopicon
