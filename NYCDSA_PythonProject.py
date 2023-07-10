<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>YelpListPrice</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>




<style type="text/css">
    pre { line-height: 125%; margin: 0; }
td.linenos pre { color: #000000; background-color: #f0f0f0; padding: 0 5px 0 5px; }
span.linenos { color: #000000; background-color: #f0f0f0; padding: 0 5px 0 5px; }
td.linenos pre.special { color: #000000; background-color: #ffffc0; padding: 0 5px 0 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding: 0 5px 0 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>



<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/*
 * Webkit scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-corner {
  background: var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-thumb {
  background: rgb(var(--jp-scrollbar-thumb-color));
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-right: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-bottom: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar */

[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-corner,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-corner {
  background-color: transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-thumb,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid transparent;
  border-right: var(--jp-scrollbar-endpad) solid transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid transparent;
  border-bottom: var(--jp-scrollbar-endpad) solid transparent;
}

/*
 * Phosphor
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Widget, /* </DEPRECATED> */
.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


/* <DEPRECATED> */ .p-Widget.p-mod-hidden, /* </DEPRECATED> */
.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-CommandPalette, /* </DEPRECATED> */
.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-CommandPalette-search, /* </DEPRECATED> */
.lm-CommandPalette-search {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-content, /* </DEPRECATED> */
.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-CommandPalette-header, /* </DEPRECATED> */
.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


/* <DEPRECATED> */ .p-CommandPalette-item, /* </DEPRECATED> */
.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


/* <DEPRECATED> */ .p-CommandPalette-itemIcon, /* </DEPRECATED> */
.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemContent, /* </DEPRECATED> */
.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


/* <DEPRECATED> */ .p-CommandPalette-itemShortcut, /* </DEPRECATED> */
.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemLabel, /* </DEPRECATED> */
.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-DockPanel, /* </DEPRECATED> */
.lm-DockPanel {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-widget, /* </DEPRECATED> */
.lm-DockPanel-widget {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-tabBar, /* </DEPRECATED> */
.lm-DockPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-DockPanel-handle, /* </DEPRECATED> */
.lm-DockPanel-handle {
  z-index: 2;
}


/* <DEPRECATED> */ .p-DockPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-DockPanel-handle:after, /* </DEPRECATED> */
.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


/* <DEPRECATED> */ .p-DockPanel-overlay, /* </DEPRECATED> */
.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


/* <DEPRECATED> */ .p-DockPanel-overlay.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Menu, /* </DEPRECATED> */
.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-Menu-content, /* </DEPRECATED> */
.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-Menu-item, /* </DEPRECATED> */
.lm-Menu-item {
  display: table-row;
}


/* <DEPRECATED> */
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed,
/* </DEPRECATED> */
.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}


/* <DEPRECATED> */
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon,
/* </DEPRECATED> */
.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


/* <DEPRECATED> */ .p-Menu-itemLabel, /* </DEPRECATED> */
.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


/* <DEPRECATED> */ .p-Menu-itemShortcut, /* </DEPRECATED> */
.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-MenuBar, /* </DEPRECATED> */
.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-MenuBar-content, /* </DEPRECATED> */
.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


/* <DEPRECATED> */ .p--MenuBar-item, /* </DEPRECATED> */
.lm-MenuBar-item {
  box-sizing: border-box;
}


/* <DEPRECATED> */
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel,
/* </DEPRECATED> */
.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-ScrollBar, /* </DEPRECATED> */
.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-ScrollBar-button, /* </DEPRECATED> */
.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-track, /* </DEPRECATED> */
.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-thumb, /* </DEPRECATED> */
.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-SplitPanel-child, /* </DEPRECATED> */
.lm-SplitPanel-child {
  z-index: 0;
}


/* <DEPRECATED> */ .p-SplitPanel-handle, /* </DEPRECATED> */
.lm-SplitPanel-handle {
  z-index: 1;
}


/* <DEPRECATED> */ .p-SplitPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-SplitPanel-handle:after, /* </DEPRECATED> */
.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabBar, /* </DEPRECATED> */
.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-content, /* </DEPRECATED> */
.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


/* <DEPRECATED> */
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-TabBar-tabLabel, /* </DEPRECATED> */
.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


/* <DEPRECATED> */ .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabPanel-tabBar, /* </DEPRECATED> */
.lm-TabPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-TabPanel-stackedPanel, /* </DEPRECATED> */
.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

@charset "UTF-8";
/*!

Copyright 2015-present Palantir Technologies, Inc. All rights reserved.
Licensed under the Apache License, Version 2.0.

*/
html{
  -webkit-box-sizing:border-box;
          box-sizing:border-box; }

*,
*::before,
*::after{
  -webkit-box-sizing:inherit;
          box-sizing:inherit; }

body{
  text-transform:none;
  line-height:1.28581;
  letter-spacing:0;
  font-size:14px;
  font-weight:400;
  color:#182026;
  font-family:-apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", "Icons16", sans-serif; }

p{
  margin-top:0;
  margin-bottom:10px; }

small{
  font-size:12px; }

strong{
  font-weight:600; }

::-moz-selection{
  background:rgba(125, 188, 255, 0.6); }

::selection{
  background:rgba(125, 188, 255, 0.6); }
.bp3-heading{
  color:#182026;
  font-weight:600;
  margin:0 0 10px;
  padding:0; }
  .bp3-dark .bp3-heading{
    color:#f5f8fa; }

h1.bp3-heading, .bp3-running-text h1{
  line-height:40px;
  font-size:36px; }

h2.bp3-heading, .bp3-running-text h2{
  line-height:32px;
  font-size:28px; }

h3.bp3-heading, .bp3-running-text h3{
  line-height:25px;
  font-size:22px; }

h4.bp3-heading, .bp3-running-text h4{
  line-height:21px;
  font-size:18px; }

h5.bp3-heading, .bp3-running-text h5{
  line-height:19px;
  font-size:16px; }

h6.bp3-heading, .bp3-running-text h6{
  line-height:16px;
  font-size:14px; }
.bp3-ui-text{
  text-transform:none;
  line-height:1.28581;
  letter-spacing:0;
  font-size:14px;
  font-weight:400; }

.bp3-monospace-text{
  text-transform:none;
  font-family:monospace; }

.bp3-text-muted{
  color:#5c7080; }
  .bp3-dark .bp3-text-muted{
    color:#a7b6c2; }

.bp3-text-disabled{
  color:rgba(92, 112, 128, 0.6); }
  .bp3-dark .bp3-text-disabled{
    color:rgba(167, 182, 194, 0.6); }

.bp3-text-overflow-ellipsis{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal; }
.bp3-running-text{
  line-height:1.5;
  font-size:14px; }
  .bp3-running-text h1{
    color:#182026;
    font-weight:600;
    margin-top:40px;
    margin-bottom:20px; }
    .bp3-dark .bp3-running-text h1{
      color:#f5f8fa; }
  .bp3-running-text h2{
    color:#182026;
    font-weight:600;
    margin-top:40px;
    margin-bottom:20px; }
    .bp3-dark .bp3-running-text h2{
      color:#f5f8fa; }
  .bp3-running-text h3{
    color:#182026;
    font-weight:600;
    margin-top:40px;
    margin-bottom:20px; }
    .bp3-dark .bp3-running-text h3{
      color:#f5f8fa; }
  .bp3-running-text h4{
    color:#182026;
    font-weight:600;
    margin-top:40px;
    margin-bottom:20px; }
    .bp3-dark .bp3-running-text h4{
      color:#f5f8fa; }
  .bp3-running-text h5{
    color:#182026;
    font-weight:600;
    margin-top:40px;
    margin-bottom:20px; }
    .bp3-dark .bp3-running-text h5{
      color:#f5f8fa; }
  .bp3-running-text h6{
    color:#182026;
    font-weight:600;
    margin-top:40px;
    margin-bottom:20px; }
    .bp3-dark .bp3-running-text h6{
      color:#f5f8fa; }
  .bp3-running-text hr{
    margin:20px 0;
    border:none;
    border-bottom:1px solid rgba(16, 22, 26, 0.15); }
    .bp3-dark .bp3-running-text hr{
      border-color:rgba(255, 255, 255, 0.15); }
  .bp3-running-text p{
    margin:0 0 10px;
    padding:0; }

.bp3-text-large{
  font-size:16px; }

.bp3-text-small{
  font-size:12px; }
a{
  text-decoration:none;
  color:#106ba3; }
  a:hover{
    cursor:pointer;
    text-decoration:underline;
    color:#106ba3; }
  a .bp3-icon, a .bp3-icon-standard, a .bp3-icon-large{
    color:inherit; }
  a code,
  .bp3-dark a code{
    color:inherit; }
  .bp3-dark a,
  .bp3-dark a:hover{
    color:#48aff0; }
    .bp3-dark a .bp3-icon, .bp3-dark a .bp3-icon-standard, .bp3-dark a .bp3-icon-large,
    .bp3-dark a:hover .bp3-icon,
    .bp3-dark a:hover .bp3-icon-standard,
    .bp3-dark a:hover .bp3-icon-large{
      color:inherit; }
.bp3-running-text code, .bp3-code{
  text-transform:none;
  font-family:monospace;
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
  background:rgba(255, 255, 255, 0.7);
  padding:2px 5px;
  color:#5c7080;
  font-size:smaller; }
  .bp3-dark .bp3-running-text code, .bp3-running-text .bp3-dark code, .bp3-dark .bp3-code{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    background:rgba(16, 22, 26, 0.3);
    color:#a7b6c2; }
  .bp3-running-text a > code, a > .bp3-code{
    color:#137cbd; }
    .bp3-dark .bp3-running-text a > code, .bp3-running-text .bp3-dark a > code, .bp3-dark a > .bp3-code{
      color:inherit; }

.bp3-running-text pre, .bp3-code-block{
  text-transform:none;
  font-family:monospace;
  display:block;
  margin:10px 0;
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
  background:rgba(255, 255, 255, 0.7);
  padding:13px 15px 12px;
  line-height:1.4;
  color:#182026;
  font-size:13px;
  word-break:break-all;
  word-wrap:break-word; }
  .bp3-dark .bp3-running-text pre, .bp3-running-text .bp3-dark pre, .bp3-dark .bp3-code-block{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    background:rgba(16, 22, 26, 0.3);
    color:#f5f8fa; }
  .bp3-running-text pre > code, .bp3-code-block > code{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:none;
    padding:0;
    color:inherit;
    font-size:inherit; }

.bp3-running-text kbd, .bp3-key{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  background:#ffffff;
  min-width:24px;
  height:24px;
  padding:3px 6px;
  vertical-align:middle;
  line-height:24px;
  color:#5c7080;
  font-family:inherit;
  font-size:12px; }
  .bp3-running-text kbd .bp3-icon, .bp3-key .bp3-icon, .bp3-running-text kbd .bp3-icon-standard, .bp3-key .bp3-icon-standard, .bp3-running-text kbd .bp3-icon-large, .bp3-key .bp3-icon-large{
    margin-right:5px; }
  .bp3-dark .bp3-running-text kbd, .bp3-running-text .bp3-dark kbd, .bp3-dark .bp3-key{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
    background:#394b59;
    color:#a7b6c2; }
.bp3-running-text blockquote, .bp3-blockquote{
  margin:0 0 10px;
  border-left:solid 4px rgba(167, 182, 194, 0.5);
  padding:0 20px; }
  .bp3-dark .bp3-running-text blockquote, .bp3-running-text .bp3-dark blockquote, .bp3-dark .bp3-blockquote{
    border-color:rgba(115, 134, 148, 0.5); }
.bp3-running-text ul,
.bp3-running-text ol, .bp3-list{
  margin:10px 0;
  padding-left:30px; }
  .bp3-running-text ul li:not(:last-child), .bp3-running-text ol li:not(:last-child), .bp3-list li:not(:last-child){
    margin-bottom:5px; }
  .bp3-running-text ul ol, .bp3-running-text ol ol, .bp3-list ol,
  .bp3-running-text ul ul,
  .bp3-running-text ol ul,
  .bp3-list ul{
    margin-top:5px; }

.bp3-list-unstyled{
  margin:0;
  padding:0;
  list-style:none; }
  .bp3-list-unstyled li{
    padding:0; }
.bp3-rtl{
  text-align:right; }

.bp3-dark{
  color:#f5f8fa; }

:focus{
  outline:rgba(19, 124, 189, 0.6) auto 2px;
  outline-offset:2px;
  -moz-outline-radius:6px; }

.bp3-focus-disabled :focus{
  outline:none !important; }
  .bp3-focus-disabled :focus ~ .bp3-control-indicator{
    outline:none !important; }

.bp3-alert{
  max-width:400px;
  padding:20px; }

.bp3-alert-body{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-alert-body .bp3-icon{
    margin-top:0;
    margin-right:20px;
    font-size:40px; }

.bp3-alert-footer{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:reverse;
      -ms-flex-direction:row-reverse;
          flex-direction:row-reverse;
  margin-top:10px; }
  .bp3-alert-footer .bp3-button{
    margin-left:10px; }
.bp3-breadcrumbs{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:wrap;
      flex-wrap:wrap;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  margin:0;
  cursor:default;
  height:30px;
  padding:0;
  list-style:none; }
  .bp3-breadcrumbs > li{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center; }
    .bp3-breadcrumbs > li::after{
      display:block;
      margin:0 5px;
      background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.71 7.29l-4-4a1.003 1.003 0 0 0-1.42 1.42L8.59 8 5.3 11.29c-.19.18-.3.43-.3.71a1.003 1.003 0 0 0 1.71.71l4-4c.18-.18.29-.43.29-.71 0-.28-.11-.53-.29-.71z' fill='%235C7080'/%3e%3c/svg%3e");
      width:16px;
      height:16px;
      content:""; }
    .bp3-breadcrumbs > li:last-of-type::after{
      display:none; }

.bp3-breadcrumb,
.bp3-breadcrumb-current,
.bp3-breadcrumbs-collapsed{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  font-size:16px; }

.bp3-breadcrumb,
.bp3-breadcrumbs-collapsed{
  color:#5c7080; }

.bp3-breadcrumb:hover{
  text-decoration:none; }

.bp3-breadcrumb.bp3-disabled{
  cursor:not-allowed;
  color:rgba(92, 112, 128, 0.6); }

.bp3-breadcrumb .bp3-icon{
  margin-right:5px; }

.bp3-breadcrumb-current{
  color:inherit;
  font-weight:600; }
  .bp3-breadcrumb-current .bp3-input{
    vertical-align:baseline;
    font-size:inherit;
    font-weight:inherit; }

.bp3-breadcrumbs-collapsed{
  margin-right:2px;
  border:none;
  border-radius:3px;
  background:#ced9e0;
  cursor:pointer;
  padding:1px 5px;
  vertical-align:text-bottom; }
  .bp3-breadcrumbs-collapsed::before{
    display:block;
    background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cg fill='%235C7080'%3e%3ccircle cx='2' cy='8.03' r='2'/%3e%3ccircle cx='14' cy='8.03' r='2'/%3e%3ccircle cx='8' cy='8.03' r='2'/%3e%3c/g%3e%3c/svg%3e") center no-repeat;
    width:16px;
    height:16px;
    content:""; }
  .bp3-breadcrumbs-collapsed:hover{
    background:#bfccd6;
    text-decoration:none;
    color:#182026; }

.bp3-dark .bp3-breadcrumb,
.bp3-dark .bp3-breadcrumbs-collapsed{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumbs > li::after{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumb.bp3-disabled{
  color:rgba(167, 182, 194, 0.6); }

.bp3-dark .bp3-breadcrumb-current{
  color:#f5f8fa; }

.bp3-dark .bp3-breadcrumbs-collapsed{
  background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-breadcrumbs-collapsed:hover{
    background:rgba(16, 22, 26, 0.6);
    color:#f5f8fa; }
.bp3-button{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  padding:5px 10px;
  vertical-align:middle;
  text-align:left;
  font-size:14px;
  min-width:30px;
  min-height:30px; }
  .bp3-button > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-button > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-button::before,
  .bp3-button > *{
    margin-right:7px; }
  .bp3-button:empty::before,
  .bp3-button > :last-child{
    margin-right:0; }
  .bp3-button:empty{
    padding:0 !important; }
  .bp3-button:disabled, .bp3-button.bp3-disabled{
    cursor:not-allowed; }
  .bp3-button.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button.bp3-align-right,
  .bp3-align-right .bp3-button{
    text-align:right; }
  .bp3-button.bp3-align-left,
  .bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-button:not([class*="bp3-intent-"]){
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    color:#182026; }
    .bp3-button:not([class*="bp3-intent-"]):hover{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
      background-clip:padding-box;
      background-color:#ebf1f5; }
    .bp3-button:not([class*="bp3-intent-"]):active, .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#d8e1e8;
      background-image:none; }
    .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      outline:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      cursor:not-allowed;
      color:rgba(92, 112, 128, 0.6); }
      .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active:hover, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-button.bp3-intent-primary{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover, .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
      background-color:#106ba3; }
    .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#0e5a8a;
      background-image:none; }
    .bp3-button.bp3-intent-primary:disabled, .bp3-button.bp3-intent-primary.bp3-disabled{
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(19, 124, 189, 0.5);
      background-image:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-success{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#0f9960;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    color:#ffffff; }
    .bp3-button.bp3-intent-success:hover, .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-success:hover{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
      background-color:#0d8050; }
    .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#0a6640;
      background-image:none; }
    .bp3-button.bp3-intent-success:disabled, .bp3-button.bp3-intent-success.bp3-disabled{
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(15, 153, 96, 0.5);
      background-image:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-warning{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#d9822b;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover, .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
      background-color:#bf7326; }
    .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#a66321;
      background-image:none; }
    .bp3-button.bp3-intent-warning:disabled, .bp3-button.bp3-intent-warning.bp3-disabled{
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(217, 130, 43, 0.5);
      background-image:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-danger{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#db3737;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover, .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
      background-color:#c23030; }
    .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#a82a2a;
      background-image:none; }
    .bp3-button.bp3-intent-danger:disabled, .bp3-button.bp3-intent-danger.bp3-disabled{
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(219, 55, 55, 0.5);
      background-image:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
    stroke:#ffffff; }
  .bp3-button.bp3-large,
  .bp3-large .bp3-button{
    min-width:40px;
    min-height:40px;
    padding:5px 15px;
    font-size:16px; }
    .bp3-button.bp3-large::before,
    .bp3-button.bp3-large > *,
    .bp3-large .bp3-button::before,
    .bp3-large .bp3-button > *{
      margin-right:10px; }
    .bp3-button.bp3-large:empty::before,
    .bp3-button.bp3-large > :last-child,
    .bp3-large .bp3-button:empty::before,
    .bp3-large .bp3-button > :last-child{
      margin-right:0; }
  .bp3-button.bp3-small,
  .bp3-small .bp3-button{
    min-width:24px;
    min-height:24px;
    padding:0 7px; }
  .bp3-button.bp3-loading{
    position:relative; }
    .bp3-button.bp3-loading[class*="bp3-icon-"]::before{
      visibility:hidden; }
    .bp3-button.bp3-loading .bp3-button-spinner{
      position:absolute;
      margin:0; }
    .bp3-button.bp3-loading > :not(.bp3-button-spinner){
      visibility:hidden; }
  .bp3-button[class*="bp3-icon-"]::before{
    line-height:1;
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-weight:400;
    font-style:normal;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    color:#5c7080; }
  .bp3-button .bp3-icon, .bp3-button .bp3-icon-standard, .bp3-button .bp3-icon-large{
    color:#5c7080; }
    .bp3-button .bp3-icon.bp3-align-right, .bp3-button .bp3-icon-standard.bp3-align-right, .bp3-button .bp3-icon-large.bp3-align-right{
      margin-left:7px; }
  .bp3-button .bp3-icon:first-child:last-child,
  .bp3-button .bp3-spinner + .bp3-icon:last-child{
    margin:0 -7px; }
  .bp3-dark .bp3-button:not([class*="bp3-intent-"]){
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover, .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      background-color:#30404d; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#202b33;
      background-image:none; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"])[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-large{
      color:#a7b6c2; }
  .bp3-dark .bp3-button[class*="bp3-intent-"]{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:active, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:disabled, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none;
      background-image:none;
      color:rgba(255, 255, 255, 0.3); }
    .bp3-dark .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
      stroke:#8a9ba8; }
  .bp3-button:disabled::before,
  .bp3-button:disabled .bp3-icon, .bp3-button:disabled .bp3-icon-standard, .bp3-button:disabled .bp3-icon-large, .bp3-button.bp3-disabled::before,
  .bp3-button.bp3-disabled .bp3-icon, .bp3-button.bp3-disabled .bp3-icon-standard, .bp3-button.bp3-disabled .bp3-icon-large, .bp3-button[class*="bp3-intent-"]::before,
  .bp3-button[class*="bp3-intent-"] .bp3-icon, .bp3-button[class*="bp3-intent-"] .bp3-icon-standard, .bp3-button[class*="bp3-intent-"] .bp3-icon-large{
    color:inherit !important; }
  .bp3-button.bp3-minimal{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:none; }
    .bp3-button.bp3-minimal:hover{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(167, 182, 194, 0.3);
      text-decoration:none;
      color:#182026; }
    .bp3-button.bp3-minimal:active, .bp3-button.bp3-minimal.bp3-active{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(115, 134, 148, 0.3);
      color:#182026; }
    .bp3-button.bp3-minimal:disabled, .bp3-button.bp3-minimal:disabled:hover, .bp3-button.bp3-minimal.bp3-disabled, .bp3-button.bp3-minimal.bp3-disabled:hover{
      background:none;
      cursor:not-allowed;
      color:rgba(92, 112, 128, 0.6); }
      .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-minimal{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-minimal:hover, .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none; }
      .bp3-dark .bp3-button.bp3-minimal:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-minimal:disabled, .bp3-dark .bp3-button.bp3-minimal:disabled:hover, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover{
        background:none;
        cursor:not-allowed;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover, .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover, .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover, .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover, .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }

a.bp3-button{
  text-align:center;
  text-decoration:none;
  -webkit-transition:none;
  transition:none; }
  a.bp3-button, a.bp3-button:hover, a.bp3-button:active{
    color:#182026; }
  a.bp3-button.bp3-disabled{
    color:rgba(92, 112, 128, 0.6); }

.bp3-button-text{
  -webkit-box-flex:0;
      -ms-flex:0 1 auto;
          flex:0 1 auto; }

.bp3-button.bp3-align-left .bp3-button-text, .bp3-button.bp3-align-right .bp3-button-text,
.bp3-button-group.bp3-align-left .bp3-button-text,
.bp3-button-group.bp3-align-right .bp3-button-text{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto; }
.bp3-button-group{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex; }
  .bp3-button-group .bp3-button{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    position:relative;
    z-index:4; }
    .bp3-button-group .bp3-button:focus{
      z-index:5; }
    .bp3-button-group .bp3-button:hover{
      z-index:6; }
    .bp3-button-group .bp3-button:active, .bp3-button-group .bp3-button.bp3-active{
      z-index:7; }
    .bp3-button-group .bp3-button:disabled, .bp3-button-group .bp3-button.bp3-disabled{
      z-index:3; }
    .bp3-button-group .bp3-button[class*="bp3-intent-"]{
      z-index:9; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:focus{
        z-index:10; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:hover{
        z-index:11; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:active, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-active{
        z-index:12; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:disabled, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-disabled{
        z-index:8; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:first-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:first-child){
    border-top-left-radius:0;
    border-bottom-left-radius:0; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    margin-right:-1px;
    border-top-right-radius:0;
    border-bottom-right-radius:0; }
  .bp3-button-group.bp3-minimal .bp3-button{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:none; }
    .bp3-button-group.bp3-minimal .bp3-button:hover{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(167, 182, 194, 0.3);
      text-decoration:none;
      color:#182026; }
    .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(115, 134, 148, 0.3);
      color:#182026; }
    .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
      background:none;
      cursor:not-allowed;
      color:rgba(92, 112, 128, 0.6); }
      .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button-group.bp3-minimal .bp3-button{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:none;
      color:inherit; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
        background:none;
        cursor:not-allowed;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
      color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
      color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:none;
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button-group .bp3-popover-wrapper,
  .bp3-button-group .bp3-popover-target{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button-group .bp3-button.bp3-fill,
  .bp3-button-group.bp3-fill .bp3-button:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-vertical{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column;
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    vertical-align:top; }
    .bp3-button-group.bp3-vertical.bp3-fill{
      width:unset;
      height:100%; }
    .bp3-button-group.bp3-vertical .bp3-button{
      margin-right:0 !important;
      width:100%; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:first-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:first-child{
      border-radius:3px 3px 0 0; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:last-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:last-child{
      border-radius:0 0 3px 3px; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:not(:last-child){
      margin-bottom:-1px; }
  .bp3-button-group.bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    margin-right:1px; }
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-button:not(:last-child){
    margin-bottom:1px; }
.bp3-callout{
  line-height:1.5;
  font-size:14px;
  position:relative;
  border-radius:3px;
  background-color:rgba(138, 155, 168, 0.15);
  width:100%;
  padding:10px 12px 9px; }
  .bp3-callout[class*="bp3-icon-"]{
    padding-left:40px; }
    .bp3-callout[class*="bp3-icon-"]::before{
      line-height:1;
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-weight:400;
      font-style:normal;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      position:absolute;
      top:10px;
      left:10px;
      color:#5c7080; }
  .bp3-callout.bp3-callout-icon{
    padding-left:40px; }
    .bp3-callout.bp3-callout-icon > .bp3-icon:first-child{
      position:absolute;
      top:10px;
      left:10px;
      color:#5c7080; }
  .bp3-callout .bp3-heading{
    margin-top:0;
    margin-bottom:5px;
    line-height:20px; }
    .bp3-callout .bp3-heading:last-child{
      margin-bottom:0; }
  .bp3-dark .bp3-callout{
    background-color:rgba(138, 155, 168, 0.2); }
    .bp3-dark .bp3-callout[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
  .bp3-callout.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15); }
    .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-primary .bp3-heading{
      color:#106ba3; }
    .bp3-dark .bp3-callout.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-primary .bp3-heading{
        color:#48aff0; }
  .bp3-callout.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15); }
    .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-success .bp3-heading{
      color:#0d8050; }
    .bp3-dark .bp3-callout.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-success .bp3-heading{
        color:#3dcc91; }
  .bp3-callout.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15); }
    .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-warning .bp3-heading{
      color:#bf7326; }
    .bp3-dark .bp3-callout.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-warning .bp3-heading{
        color:#ffb366; }
  .bp3-callout.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15); }
    .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-danger .bp3-heading{
      color:#c23030; }
    .bp3-dark .bp3-callout.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-danger .bp3-heading{
        color:#ff7373; }
  .bp3-running-text .bp3-callout{
    margin:20px 0; }
.bp3-card{
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
  background-color:#ffffff;
  padding:20px;
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-card.bp3-dark,
  .bp3-dark .bp3-card{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
    background-color:#30404d; }

.bp3-elevation-0{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }
  .bp3-elevation-0.bp3-dark,
  .bp3-dark .bp3-elevation-0{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-1{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-1.bp3-dark,
  .bp3-dark .bp3-elevation-1{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-elevation-2{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-2.bp3-dark,
  .bp3-dark .bp3-elevation-2{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4); }

.bp3-elevation-3{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-3.bp3-dark,
  .bp3-dark .bp3-elevation-3{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-elevation-4{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-4.bp3-dark,
  .bp3-dark .bp3-elevation-4{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:hover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  cursor:pointer; }
  .bp3-card.bp3-interactive:hover.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:hover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:active{
  opacity:0.9;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  -webkit-transition-duration:0;
          transition-duration:0; }
  .bp3-card.bp3-interactive:active.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:active{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-collapse{
  height:0;
  overflow-y:hidden;
  -webkit-transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-collapse .bp3-collapse-body{
    -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-collapse .bp3-collapse-body[aria-hidden="true"]{
      display:none; }

.bp3-context-menu .bp3-popover-target{
  display:block; }

.bp3-context-menu-popover-target{
  position:fixed; }

.bp3-divider{
  margin:5px;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  border-bottom:1px solid rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-dialog-container{
  opacity:1;
  -webkit-transform:scale(1);
          transform:scale(1);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  width:100%;
  min-height:100%;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-dialog-container.bp3-overlay-enter > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5); }
  .bp3-dialog-container.bp3-overlay-enter-active > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear-active > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-dialog-container.bp3-overlay-exit > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-dialog-container.bp3-overlay-exit-active > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5);
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
    -webkit-transition-delay:0;
            transition-delay:0; }

.bp3-dialog{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:30px 0;
  border-radius:6px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  background:#ebf1f5;
  width:500px;
  padding-bottom:20px;
  pointer-events:all;
  -webkit-user-select:text;
     -moz-user-select:text;
      -ms-user-select:text;
          user-select:text; }
  .bp3-dialog:focus{
    outline:0; }
  .bp3-dialog.bp3-dark,
  .bp3-dark .bp3-dialog{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    background:#293742;
    color:#f5f8fa; }

.bp3-dialog-header{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border-radius:6px 6px 0 0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  background:#ffffff;
  min-height:40px;
  padding-right:5px;
  padding-left:20px; }
  .bp3-dialog-header .bp3-icon-large,
  .bp3-dialog-header .bp3-icon{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px;
    color:#5c7080; }
  .bp3-dialog-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    margin:0;
    line-height:inherit; }
    .bp3-dialog-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-dialog-header{
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
    background:#30404d; }
    .bp3-dark .bp3-dialog-header .bp3-icon-large,
    .bp3-dark .bp3-dialog-header .bp3-icon{
      color:#a7b6c2; }

.bp3-dialog-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  margin:20px;
  line-height:18px; }

.bp3-dialog-footer{
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  margin:0 20px; }

.bp3-dialog-footer-actions{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:end;
      -ms-flex-pack:end;
          justify-content:flex-end; }
  .bp3-dialog-footer-actions .bp3-button{
    margin-left:10px; }
.bp3-drawer{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  background:#ffffff;
  padding:0; }
  .bp3-drawer:focus{
    outline:0; }
  .bp3-drawer.bp3-position-top{
    top:0;
    right:0;
    left:0;
    height:50%; }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter, .bp3-drawer.bp3-position-top.bp3-overlay-appear{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%); }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter-active, .bp3-drawer.bp3-position-top.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit-active{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
  .bp3-drawer.bp3-position-bottom{
    right:0;
    bottom:0;
    left:0;
    height:50%; }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter-active, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
  .bp3-drawer.bp3-position-left{
    top:0;
    bottom:0;
    left:0;
    width:50%; }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter, .bp3-drawer.bp3-position-left.bp3-overlay-appear{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%); }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter-active, .bp3-drawer.bp3-position-left.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit-active{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
  .bp3-drawer.bp3-position-right{
    top:0;
    right:0;
    bottom:0;
    width:50%; }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter, .bp3-drawer.bp3-position-right.bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter-active, .bp3-drawer.bp3-position-right.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right):not(.bp3-vertical){
    top:0;
    right:0;
    bottom:0;
    width:50%; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right).bp3-vertical{
    right:0;
    bottom:0;
    left:0;
    height:50%; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
      -webkit-transition-delay:0;
              transition-delay:0; }
  .bp3-drawer.bp3-dark,
  .bp3-dark .bp3-drawer{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    background:#30404d;
    color:#f5f8fa; }

.bp3-drawer-header{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  position:relative;
  border-radius:0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  min-height:40px;
  padding:5px;
  padding-left:20px; }
  .bp3-drawer-header .bp3-icon-large,
  .bp3-drawer-header .bp3-icon{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px;
    color:#5c7080; }
  .bp3-drawer-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    margin:0;
    line-height:inherit; }
    .bp3-drawer-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-drawer-header{
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-drawer-header .bp3-icon-large,
    .bp3-dark .bp3-drawer-header .bp3-icon{
      color:#a7b6c2; }

.bp3-drawer-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  overflow:auto;
  line-height:18px; }

.bp3-drawer-footer{
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  position:relative;
  -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
  padding:10px 20px; }
  .bp3-dark .bp3-drawer-footer{
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4); }
.bp3-editable-text{
  display:inline-block;
  position:relative;
  cursor:text;
  max-width:100%;
  vertical-align:top;
  white-space:nowrap; }
  .bp3-editable-text::before{
    position:absolute;
    top:-3px;
    right:-3px;
    bottom:-3px;
    left:-3px;
    border-radius:3px;
    content:"";
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-editable-text.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
    background-color:#ffffff; }
  .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#137cbd; }
  .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4); }
  .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#0f9960; }
  .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4); }
  .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#d9822b; }
  .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4); }
  .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#db3737; }
  .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4); }
  .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15); }
  .bp3-dark .bp3-editable-text.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    background-color:rgba(16, 22, 26, 0.3); }
  .bp3-dark .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#48aff0; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4);
            box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#3dcc91; }
  .bp3-dark .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4);
            box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#ffb366; }
  .bp3-dark .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4);
            box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#ff7373; }
  .bp3-dark .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4);
            box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-editable-text-input,
.bp3-editable-text-content{
  display:inherit;
  position:relative;
  min-width:inherit;
  max-width:inherit;
  vertical-align:top;
  text-transform:inherit;
  letter-spacing:inherit;
  color:inherit;
  font:inherit;
  resize:none; }

.bp3-editable-text-input{
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  background:none;
  width:100%;
  padding:0;
  white-space:pre-wrap; }
  .bp3-editable-text-input::-webkit-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-editable-text-input::-moz-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-editable-text-input:-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-editable-text-input::-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-editable-text-input::placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-editable-text-input:focus{
    outline:none; }
  .bp3-editable-text-input::-ms-clear{
    display:none; }

.bp3-editable-text-content{
  overflow:hidden;
  padding-right:2px;
  text-overflow:ellipsis;
  white-space:pre; }
  .bp3-editable-text-editing > .bp3-editable-text-content{
    position:absolute;
    left:0;
    visibility:hidden; }
  .bp3-editable-text-placeholder > .bp3-editable-text-content{
    color:rgba(92, 112, 128, 0.6); }
    .bp3-dark .bp3-editable-text-placeholder > .bp3-editable-text-content{
      color:rgba(167, 182, 194, 0.6); }

.bp3-editable-text.bp3-multiline{
  display:block; }
  .bp3-editable-text.bp3-multiline .bp3-editable-text-content{
    overflow:auto;
    white-space:pre-wrap;
    word-wrap:break-word; }
.bp3-control-group{
  -webkit-transform:translateZ(0);
          transform:translateZ(0);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:stretch;
      -ms-flex-align:stretch;
          align-items:stretch; }
  .bp3-control-group > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select,
  .bp3-control-group .bp3-input,
  .bp3-control-group .bp3-select{
    position:relative; }
  .bp3-control-group .bp3-input{
    z-index:2;
    border-radius:inherit; }
    .bp3-control-group .bp3-input:focus{
      z-index:14;
      border-radius:3px; }
    .bp3-control-group .bp3-input[class*="bp3-intent"]{
      z-index:13; }
      .bp3-control-group .bp3-input[class*="bp3-intent"]:focus{
        z-index:15; }
    .bp3-control-group .bp3-input[readonly], .bp3-control-group .bp3-input:disabled, .bp3-control-group .bp3-input.bp3-disabled{
      z-index:1; }
  .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input{
    z-index:13; }
    .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input:focus{
      z-index:15; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select select,
  .bp3-control-group .bp3-select select{
    -webkit-transform:translateZ(0);
            transform:translateZ(0);
    z-index:4;
    border-radius:inherit; }
    .bp3-control-group .bp3-button:focus,
    .bp3-control-group .bp3-html-select select:focus,
    .bp3-control-group .bp3-select select:focus{
      z-index:5; }
    .bp3-control-group .bp3-button:hover,
    .bp3-control-group .bp3-html-select select:hover,
    .bp3-control-group .bp3-select select:hover{
      z-index:6; }
    .bp3-control-group .bp3-button:active,
    .bp3-control-group .bp3-html-select select:active,
    .bp3-control-group .bp3-select select:active{
      z-index:7; }
    .bp3-control-group .bp3-button[readonly], .bp3-control-group .bp3-button:disabled, .bp3-control-group .bp3-button.bp3-disabled,
    .bp3-control-group .bp3-html-select select[readonly],
    .bp3-control-group .bp3-html-select select:disabled,
    .bp3-control-group .bp3-html-select select.bp3-disabled,
    .bp3-control-group .bp3-select select[readonly],
    .bp3-control-group .bp3-select select:disabled,
    .bp3-control-group .bp3-select select.bp3-disabled{
      z-index:3; }
    .bp3-control-group .bp3-button[class*="bp3-intent"],
    .bp3-control-group .bp3-html-select select[class*="bp3-intent"],
    .bp3-control-group .bp3-select select[class*="bp3-intent"]{
      z-index:9; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:focus{
        z-index:10; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:hover{
        z-index:11; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:active{
        z-index:12; }
      .bp3-control-group .bp3-button[class*="bp3-intent"][readonly], .bp3-control-group .bp3-button[class*="bp3-intent"]:disabled, .bp3-control-group .bp3-button[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"].bp3-disabled{
        z-index:8; }
  .bp3-control-group .bp3-input-group > .bp3-icon,
  .bp3-control-group .bp3-input-group > .bp3-button,
  .bp3-control-group .bp3-input-group > .bp3-input-action{
    z-index:16; }
  .bp3-control-group .bp3-select::after,
  .bp3-control-group .bp3-html-select::after,
  .bp3-control-group .bp3-select > .bp3-icon,
  .bp3-control-group .bp3-html-select > .bp3-icon{
    z-index:17; }
  .bp3-control-group:not(.bp3-vertical) > *{
    margin-right:-1px; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > *{
    margin-right:0; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > .bp3-button + .bp3-button{
    margin-left:1px; }
  .bp3-control-group .bp3-popover-wrapper,
  .bp3-control-group .bp3-popover-target{
    border-radius:inherit; }
  .bp3-control-group > :first-child{
    border-radius:3px 0 0 3px; }
  .bp3-control-group > :last-child{
    margin-right:0;
    border-radius:0 3px 3px 0; }
  .bp3-control-group > :only-child{
    margin-right:0;
    border-radius:3px; }
  .bp3-control-group .bp3-input-group .bp3-button{
    border-radius:3px; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-fill > *:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-vertical{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-control-group.bp3-vertical > *{
      margin-top:-1px; }
    .bp3-control-group.bp3-vertical > :first-child{
      margin-top:0;
      border-radius:3px 3px 0 0; }
    .bp3-control-group.bp3-vertical > :last-child{
      border-radius:0 0 3px 3px; }
.bp3-control{
  display:block;
  position:relative;
  margin-bottom:10px;
  cursor:pointer;
  text-transform:none; }
  .bp3-control input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    color:#ffffff; }
  .bp3-control:hover input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#106ba3; }
  .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background:#0e5a8a; }
  .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(19, 124, 189, 0.5); }
  .bp3-dark .bp3-control input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control:hover input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    background-color:#106ba3; }
  .bp3-dark .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background-color:#0e5a8a; }
  .bp3-dark .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(14, 90, 138, 0.5); }
  .bp3-control:not(.bp3-align-right){
    padding-left:26px; }
    .bp3-control:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-26px; }
  .bp3-control.bp3-align-right{
    padding-right:26px; }
    .bp3-control.bp3-align-right .bp3-control-indicator{
      margin-right:-26px; }
  .bp3-control.bp3-disabled{
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-control.bp3-inline{
    display:inline-block;
    margin-right:20px; }
  .bp3-control input{
    position:absolute;
    top:0;
    left:0;
    opacity:0;
    z-index:-1; }
  .bp3-control .bp3-control-indicator{
    display:inline-block;
    position:relative;
    margin-top:-3px;
    margin-right:10px;
    border:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    background-clip:padding-box;
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    cursor:pointer;
    width:1em;
    height:1em;
    vertical-align:middle;
    font-size:16px;
    -webkit-user-select:none;
       -moz-user-select:none;
        -ms-user-select:none;
            user-select:none; }
    .bp3-control .bp3-control-indicator::before{
      display:block;
      width:1em;
      height:1em;
      content:""; }
  .bp3-control:hover .bp3-control-indicator{
    background-color:#ebf1f5; }
  .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background:#d8e1e8; }
  .bp3-control input:disabled ~ .bp3-control-indicator{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(206, 217, 224, 0.5);
    cursor:not-allowed; }
  .bp3-control input:focus ~ .bp3-control-indicator{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:2px;
    -moz-outline-radius:6px; }
  .bp3-control.bp3-align-right .bp3-control-indicator{
    float:right;
    margin-top:1px;
    margin-left:10px; }
  .bp3-control.bp3-large{
    font-size:16px; }
    .bp3-control.bp3-large:not(.bp3-align-right){
      padding-left:30px; }
      .bp3-control.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
        margin-left:-30px; }
    .bp3-control.bp3-large.bp3-align-right{
      padding-right:30px; }
      .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
        margin-right:-30px; }
    .bp3-control.bp3-large .bp3-control-indicator{
      font-size:20px; }
    .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-top:0; }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    color:#ffffff; }
  .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    background-color:#106ba3; }
  .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background:#0e5a8a; }
  .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(19, 124, 189, 0.5); }
  .bp3-dark .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    background-color:#106ba3; }
  .bp3-dark .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background-color:#0e5a8a; }
  .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(14, 90, 138, 0.5); }
  .bp3-control.bp3-checkbox .bp3-control-indicator{
    border-radius:3px; }
  .bp3-control.bp3-checkbox input:checked ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M12 5c-.28 0-.53.11-.71.29L7 9.59l-2.29-2.3a1.003 1.003 0 0 0-1.42 1.42l3 3c.18.18.43.29.71.29s.53-.11.71-.29l5-5A1.003 1.003 0 0 0 12 5z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M11 7H5c-.55 0-1 .45-1 1s.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-radio .bp3-control-indicator{
    border-radius:50%; }
  .bp3-control.bp3-radio input:checked ~ .bp3-control-indicator::before{
    background-image:radial-gradient(#ffffff, #ffffff 28%, transparent 32%); }
  .bp3-control.bp3-radio input:checked:disabled ~ .bp3-control-indicator::before{
    opacity:0.5; }
  .bp3-control.bp3-radio input:focus ~ .bp3-control-indicator{
    -moz-outline-radius:16px; }
  .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(167, 182, 194, 0.5); }
  .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(115, 134, 148, 0.5); }
  .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(92, 112, 128, 0.5); }
  .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5); }
    .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5); }
    .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch:not(.bp3-align-right){
    padding-left:38px; }
    .bp3-control.bp3-switch:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-38px; }
  .bp3-control.bp3-switch.bp3-align-right{
    padding-right:38px; }
    .bp3-control.bp3-switch.bp3-align-right .bp3-control-indicator{
      margin-right:-38px; }
  .bp3-control.bp3-switch .bp3-control-indicator{
    border:none;
    border-radius:1.75em;
    -webkit-box-shadow:none !important;
            box-shadow:none !important;
    width:auto;
    min-width:1.75em;
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-control.bp3-switch .bp3-control-indicator::before{
      position:absolute;
      left:0;
      margin:2px;
      border-radius:50%;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
      background:#ffffff;
      width:calc(1em - 4px);
      height:calc(1em - 4px);
      -webkit-transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    left:calc(100% - 1em); }
  .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right){
    padding-left:45px; }
    .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-45px; }
  .bp3-control.bp3-switch.bp3-large.bp3-align-right{
    padding-right:45px; }
    .bp3-control.bp3-switch.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-right:-45px; }
  .bp3-dark .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.7); }
  .bp3-dark .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.9); }
  .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(57, 75, 89, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-dark .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-dark .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch .bp3-control-indicator::before{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    background:#394b59; }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-control.bp3-switch .bp3-switch-inner-text{
    text-align:center;
    font-size:0.7em; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:first-child{
    visibility:hidden;
    margin-right:1.2em;
    margin-left:0.5em;
    line-height:0; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:last-child{
    visibility:visible;
    margin-right:0.5em;
    margin-left:1.2em;
    line-height:1em; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:first-child{
    visibility:visible;
    line-height:1em; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:last-child{
    visibility:hidden;
    line-height:0; }
  .bp3-dark .bp3-control{
    color:#f5f8fa; }
    .bp3-dark .bp3-control.bp3-disabled{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-control .bp3-control-indicator{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0)); }
    .bp3-dark .bp3-control:hover .bp3-control-indicator{
      background-color:#30404d; }
    .bp3-dark .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background:#202b33; }
    .bp3-dark .bp3-control input:disabled ~ .bp3-control-indicator{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(57, 75, 89, 0.5);
      cursor:not-allowed; }
    .bp3-dark .bp3-control.bp3-checkbox input:disabled:checked ~ .bp3-control-indicator, .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
      color:rgba(167, 182, 194, 0.6); }
.bp3-file-input{
  display:inline-block;
  position:relative;
  cursor:pointer;
  height:30px; }
  .bp3-file-input input{
    opacity:0;
    margin:0;
    min-width:200px; }
    .bp3-file-input input:disabled + .bp3-file-upload-input,
    .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(206, 217, 224, 0.5);
      cursor:not-allowed;
      color:rgba(92, 112, 128, 0.6);
      resize:none; }
      .bp3-file-input input:disabled + .bp3-file-upload-input::after,
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
        outline:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        background-color:rgba(206, 217, 224, 0.5);
        background-image:none;
        cursor:not-allowed;
        color:rgba(92, 112, 128, 0.6); }
        .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active:hover,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active:hover{
          background:rgba(206, 217, 224, 0.7); }
      .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input, .bp3-dark
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
        -webkit-box-shadow:none;
                box-shadow:none;
        background:rgba(57, 75, 89, 0.5);
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after, .bp3-dark
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
          -webkit-box-shadow:none;
                  box-shadow:none;
          background-color:rgba(57, 75, 89, 0.5);
          background-image:none;
          color:rgba(167, 182, 194, 0.6); }
          .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-dark
          .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active{
            background:rgba(57, 75, 89, 0.7); }
  .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#182026; }
  .bp3-dark .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#f5f8fa; }
  .bp3-file-input.bp3-fill{
    width:100%; }
  .bp3-file-input.bp3-large,
  .bp3-large .bp3-file-input{
    height:40px; }
  .bp3-file-input .bp3-file-upload-input-custom-text::after{
    content:attr(bp3-button-text); }

.bp3-file-upload-input{
  outline:none;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  background:#ffffff;
  height:30px;
  padding:0 10px;
  vertical-align:middle;
  line-height:30px;
  color:#182026;
  font-size:14px;
  font-weight:400;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  position:absolute;
  top:0;
  right:0;
  left:0;
  padding-right:80px;
  color:rgba(92, 112, 128, 0.6);
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-file-upload-input::-webkit-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-file-upload-input::-moz-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-file-upload-input:-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-file-upload-input::-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-file-upload-input::placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-file-upload-input:focus, .bp3-file-upload-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-file-upload-input[type="search"], .bp3-file-upload-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-file-upload-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-file-upload-input:disabled, .bp3-file-upload-input.bp3-disabled{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(206, 217, 224, 0.5);
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6);
    resize:none; }
  .bp3-file-upload-input::after{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    color:#182026;
    min-width:24px;
    min-height:24px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    position:absolute;
    top:0;
    right:0;
    margin:3px;
    border-radius:3px;
    width:70px;
    text-align:center;
    line-height:24px;
    content:"Browse"; }
    .bp3-file-upload-input::after:hover{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
      background-clip:padding-box;
      background-color:#ebf1f5; }
    .bp3-file-upload-input::after:active, .bp3-file-upload-input::after.bp3-active{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#d8e1e8;
      background-image:none; }
    .bp3-file-upload-input::after:disabled, .bp3-file-upload-input::after.bp3-disabled{
      outline:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      cursor:not-allowed;
      color:rgba(92, 112, 128, 0.6); }
      .bp3-file-upload-input::after:disabled.bp3-active, .bp3-file-upload-input::after:disabled.bp3-active:hover, .bp3-file-upload-input::after.bp3-disabled.bp3-active, .bp3-file-upload-input::after.bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-file-upload-input:hover::after{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    background-clip:padding-box;
    background-color:#ebf1f5; }
  .bp3-file-upload-input:active::after{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background-color:#d8e1e8;
    background-image:none; }
  .bp3-large .bp3-file-upload-input{
    height:40px;
    line-height:40px;
    font-size:16px;
    padding-right:95px; }
    .bp3-large .bp3-file-upload-input[type="search"], .bp3-large .bp3-file-upload-input.bp3-round{
      padding:0 15px; }
    .bp3-large .bp3-file-upload-input::after{
      min-width:30px;
      min-height:30px;
      margin:5px;
      width:85px;
      line-height:30px; }
  .bp3-dark .bp3-file-upload-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    background:rgba(16, 22, 26, 0.3);
    color:#f5f8fa;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:disabled, .bp3-dark .bp3-file-upload-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(57, 75, 89, 0.5);
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::after{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover, .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover{
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
        background-color:#30404d; }
      .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
        background-color:#202b33;
        background-image:none; }
      .bp3-dark .bp3-file-upload-input::after:disabled, .bp3-dark .bp3-file-upload-input::after.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none;
        background-color:rgba(57, 75, 89, 0.5);
        background-image:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-upload-input::after:disabled.bp3-active, .bp3-dark .bp3-file-upload-input::after.bp3-disabled.bp3-active{
          background:rgba(57, 75, 89, 0.7); }
      .bp3-dark .bp3-file-upload-input::after .bp3-button-spinner .bp3-spinner-head{
        background:rgba(16, 22, 26, 0.5);
        stroke:#8a9ba8; }
    .bp3-dark .bp3-file-upload-input:hover::after{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      background-color:#30404d; }
    .bp3-dark .bp3-file-upload-input:active::after{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#202b33;
      background-image:none; }

.bp3-file-upload-input::after{
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
.bp3-form-group{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0 0 15px; }
  .bp3-form-group label.bp3-label{
    margin-bottom:5px; }
  .bp3-form-group .bp3-control{
    margin-top:7px; }
  .bp3-form-group .bp3-form-helper-text{
    margin-top:5px;
    color:#5c7080;
    font-size:12px; }
  .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#106ba3; }
  .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#0d8050; }
  .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#bf7326; }
  .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#c23030; }
  .bp3-form-group.bp3-inline{
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row;
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
    .bp3-form-group.bp3-inline.bp3-large label.bp3-label{
      margin:0 10px 0 0;
      line-height:40px; }
    .bp3-form-group.bp3-inline label.bp3-label{
      margin:0 10px 0 0;
      line-height:30px; }
  .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-dark .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#48aff0; }
  .bp3-dark .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#3dcc91; }
  .bp3-dark .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#ffb366; }
  .bp3-dark .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#ff7373; }
  .bp3-dark .bp3-form-group .bp3-form-helper-text{
    color:#a7b6c2; }
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(167, 182, 194, 0.6) !important; }
.bp3-input-group{
  display:block;
  position:relative; }
  .bp3-input-group .bp3-input{
    position:relative;
    width:100%; }
    .bp3-input-group .bp3-input:not(:first-child){
      padding-left:30px; }
    .bp3-input-group .bp3-input:not(:last-child){
      padding-right:30px; }
  .bp3-input-group .bp3-input-action,
  .bp3-input-group > .bp3-button,
  .bp3-input-group > .bp3-icon{
    position:absolute;
    top:0; }
    .bp3-input-group .bp3-input-action:first-child,
    .bp3-input-group > .bp3-button:first-child,
    .bp3-input-group > .bp3-icon:first-child{
      left:0; }
    .bp3-input-group .bp3-input-action:last-child,
    .bp3-input-group > .bp3-button:last-child,
    .bp3-input-group > .bp3-icon:last-child{
      right:0; }
  .bp3-input-group .bp3-button{
    min-width:24px;
    min-height:24px;
    margin:3px;
    padding:0 7px; }
    .bp3-input-group .bp3-button:empty{
      padding:0; }
  .bp3-input-group > .bp3-icon{
    z-index:1;
    color:#5c7080; }
    .bp3-input-group > .bp3-icon:empty{
      line-height:1;
      font-family:"Icons16", sans-serif;
      font-size:16px;
      font-weight:400;
      font-style:normal;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased; }
  .bp3-input-group > .bp3-icon,
  .bp3-input-group .bp3-input-action > .bp3-spinner{
    margin:7px; }
  .bp3-input-group .bp3-tag{
    margin:5px; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus),
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
    color:#5c7080; }
    .bp3-dark .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus), .bp3-dark
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
      color:#a7b6c2; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large{
      color:#5c7080; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled,
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled{
    color:rgba(92, 112, 128, 0.6) !important; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-large{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-input-group.bp3-disabled{
    cursor:not-allowed; }
    .bp3-input-group.bp3-disabled .bp3-icon{
      color:rgba(92, 112, 128, 0.6); }
  .bp3-input-group.bp3-large .bp3-button{
    min-width:30px;
    min-height:30px;
    margin:5px; }
  .bp3-input-group.bp3-large > .bp3-icon,
  .bp3-input-group.bp3-large .bp3-input-action > .bp3-spinner{
    margin:12px; }
  .bp3-input-group.bp3-large .bp3-input{
    height:40px;
    line-height:40px;
    font-size:16px; }
    .bp3-input-group.bp3-large .bp3-input[type="search"], .bp3-input-group.bp3-large .bp3-input.bp3-round{
      padding:0 15px; }
    .bp3-input-group.bp3-large .bp3-input:not(:first-child){
      padding-left:40px; }
    .bp3-input-group.bp3-large .bp3-input:not(:last-child){
      padding-right:40px; }
  .bp3-input-group.bp3-small .bp3-button{
    min-width:20px;
    min-height:20px;
    margin:2px; }
  .bp3-input-group.bp3-small .bp3-tag{
    min-width:20px;
    min-height:20px;
    margin:2px; }
  .bp3-input-group.bp3-small > .bp3-icon,
  .bp3-input-group.bp3-small .bp3-input-action > .bp3-spinner{
    margin:4px; }
  .bp3-input-group.bp3-small .bp3-input{
    height:24px;
    padding-right:8px;
    padding-left:8px;
    line-height:24px;
    font-size:12px; }
    .bp3-input-group.bp3-small .bp3-input[type="search"], .bp3-input-group.bp3-small .bp3-input.bp3-round{
      padding:0 12px; }
    .bp3-input-group.bp3-small .bp3-input:not(:first-child){
      padding-left:24px; }
    .bp3-input-group.bp3-small .bp3-input:not(:last-child){
      padding-right:24px; }
  .bp3-input-group.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-input-group.bp3-round .bp3-button,
  .bp3-input-group.bp3-round .bp3-input,
  .bp3-input-group.bp3-round .bp3-tag{
    border-radius:30px; }
  .bp3-dark .bp3-input-group .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-input-group.bp3-disabled .bp3-icon{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-input-group.bp3-intent-primary .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input-group.bp3-intent-primary .bp3-input:disabled, .bp3-input-group.bp3-intent-primary .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-primary > .bp3-icon{
    color:#106ba3; }
    .bp3-dark .bp3-input-group.bp3-intent-primary > .bp3-icon{
      color:#48aff0; }
  .bp3-input-group.bp3-intent-success .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input-group.bp3-intent-success .bp3-input:disabled, .bp3-input-group.bp3-intent-success .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-success > .bp3-icon{
    color:#0d8050; }
    .bp3-dark .bp3-input-group.bp3-intent-success > .bp3-icon{
      color:#3dcc91; }
  .bp3-input-group.bp3-intent-warning .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input-group.bp3-intent-warning .bp3-input:disabled, .bp3-input-group.bp3-intent-warning .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-warning > .bp3-icon{
    color:#bf7326; }
    .bp3-dark .bp3-input-group.bp3-intent-warning > .bp3-icon{
      color:#ffb366; }
  .bp3-input-group.bp3-intent-danger .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input-group.bp3-intent-danger .bp3-input:disabled, .bp3-input-group.bp3-intent-danger .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-danger > .bp3-icon{
    color:#c23030; }
    .bp3-dark .bp3-input-group.bp3-intent-danger > .bp3-icon{
      color:#ff7373; }
.bp3-input{
  outline:none;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  background:#ffffff;
  height:30px;
  padding:0 10px;
  vertical-align:middle;
  line-height:30px;
  color:#182026;
  font-size:14px;
  font-weight:400;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none; }
  .bp3-input::-webkit-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input::-moz-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input:-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input::-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input::placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input:focus, .bp3-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-input[type="search"], .bp3-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-input:disabled, .bp3-input.bp3-disabled{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(206, 217, 224, 0.5);
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6);
    resize:none; }
  .bp3-input.bp3-large{
    height:40px;
    line-height:40px;
    font-size:16px; }
    .bp3-input.bp3-large[type="search"], .bp3-input.bp3-large.bp3-round{
      padding:0 15px; }
  .bp3-input.bp3-small{
    height:24px;
    padding-right:8px;
    padding-left:8px;
    line-height:24px;
    font-size:12px; }
    .bp3-input.bp3-small[type="search"], .bp3-input.bp3-small.bp3-round{
      padding:0 12px; }
  .bp3-input.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-dark .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    background:rgba(16, 22, 26, 0.3);
    color:#f5f8fa; }
    .bp3-dark .bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input:disabled, .bp3-dark .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(57, 75, 89, 0.5);
      color:rgba(167, 182, 194, 0.6); }
  .bp3-input.bp3-intent-primary{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input.bp3-intent-primary:disabled, .bp3-input.bp3-intent-primary.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary:focus{
        -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #137cbd;
                box-shadow:inset 0 0 0 1px #137cbd; }
      .bp3-dark .bp3-input.bp3-intent-primary:disabled, .bp3-dark .bp3-input.bp3-intent-primary.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-success{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input.bp3-intent-success:disabled, .bp3-input.bp3-intent-success.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-success{
      -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success:focus{
        -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #0f9960;
                box-shadow:inset 0 0 0 1px #0f9960; }
      .bp3-dark .bp3-input.bp3-intent-success:disabled, .bp3-dark .bp3-input.bp3-intent-success.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-warning{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input.bp3-intent-warning:disabled, .bp3-input.bp3-intent-warning.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning:focus{
        -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #d9822b;
                box-shadow:inset 0 0 0 1px #d9822b; }
      .bp3-dark .bp3-input.bp3-intent-warning:disabled, .bp3-dark .bp3-input.bp3-intent-warning.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-danger{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input.bp3-intent-danger:disabled, .bp3-input.bp3-intent-danger.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger:focus{
        -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #db3737;
                box-shadow:inset 0 0 0 1px #db3737; }
      .bp3-dark .bp3-input.bp3-intent-danger:disabled, .bp3-dark .bp3-input.bp3-intent-danger.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input::-ms-clear{
    display:none; }
textarea.bp3-input{
  max-width:100%;
  padding:10px; }
  textarea.bp3-input, textarea.bp3-input.bp3-large, textarea.bp3-input.bp3-small{
    height:auto;
    line-height:inherit; }
  textarea.bp3-input.bp3-small{
    padding:8px; }
  .bp3-dark textarea.bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    background:rgba(16, 22, 26, 0.3);
    color:#f5f8fa; }
    .bp3-dark textarea.bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input:disabled, .bp3-dark textarea.bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:rgba(57, 75, 89, 0.5);
      color:rgba(167, 182, 194, 0.6); }
label.bp3-label{
  display:block;
  margin-top:0;
  margin-bottom:15px; }
  label.bp3-label .bp3-html-select,
  label.bp3-label .bp3-input,
  label.bp3-label .bp3-select,
  label.bp3-label .bp3-slider,
  label.bp3-label .bp3-popover-wrapper{
    display:block;
    margin-top:5px;
    text-transform:none; }
  label.bp3-label .bp3-button-group{
    margin-top:5px; }
  label.bp3-label .bp3-select select,
  label.bp3-label .bp3-html-select select{
    width:100%;
    vertical-align:top;
    font-weight:400; }
  label.bp3-label.bp3-disabled,
  label.bp3-label.bp3-disabled .bp3-text-muted{
    color:rgba(92, 112, 128, 0.6); }
  label.bp3-label.bp3-inline{
    line-height:30px; }
    label.bp3-label.bp3-inline .bp3-html-select,
    label.bp3-label.bp3-inline .bp3-input,
    label.bp3-label.bp3-inline .bp3-input-group,
    label.bp3-label.bp3-inline .bp3-select,
    label.bp3-label.bp3-inline .bp3-popover-wrapper{
      display:inline-block;
      margin:0 0 0 5px;
      vertical-align:top; }
    label.bp3-label.bp3-inline .bp3-button-group{
      margin:0 0 0 5px; }
    label.bp3-label.bp3-inline .bp3-input-group .bp3-input{
      margin-left:0; }
    label.bp3-label.bp3-inline.bp3-large{
      line-height:40px; }
  label.bp3-label:not(.bp3-inline) .bp3-popover-target{
    display:block; }
  .bp3-dark label.bp3-label{
    color:#f5f8fa; }
    .bp3-dark label.bp3-label.bp3-disabled,
    .bp3-dark label.bp3-label.bp3-disabled .bp3-text-muted{
      color:rgba(167, 182, 194, 0.6); }
.bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button{
  -webkit-box-flex:1;
      -ms-flex:1 1 14px;
          flex:1 1 14px;
  width:30px;
  min-height:0;
  padding:0; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:first-child{
    border-radius:0 3px 0 0; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:last-child{
    border-radius:0 0 3px 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:first-child{
  border-radius:3px 0 0 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:last-child{
  border-radius:0 0 0 3px; }

.bp3-numeric-input.bp3-large .bp3-button-group.bp3-vertical > .bp3-button{
  width:40px; }

form{
  display:block; }
.bp3-html-select select,
.bp3-select select{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  padding:5px 10px;
  vertical-align:middle;
  text-align:left;
  font-size:14px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  color:#182026;
  border-radius:3px;
  width:100%;
  height:30px;
  padding:0 25px 0 10px;
  -moz-appearance:none;
  -webkit-appearance:none; }
  .bp3-html-select select > *, .bp3-select select > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-html-select select > .bp3-fill, .bp3-select select > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-html-select select::before,
  .bp3-select select::before, .bp3-html-select select > *, .bp3-select select > *{
    margin-right:7px; }
  .bp3-html-select select:empty::before,
  .bp3-select select:empty::before,
  .bp3-html-select select > :last-child,
  .bp3-select select > :last-child{
    margin-right:0; }
  .bp3-html-select select:hover,
  .bp3-select select:hover{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    background-clip:padding-box;
    background-color:#ebf1f5; }
  .bp3-html-select select:active,
  .bp3-select select:active, .bp3-html-select select.bp3-active,
  .bp3-select select.bp3-active{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background-color:#d8e1e8;
    background-image:none; }
  .bp3-html-select select:disabled,
  .bp3-select select:disabled, .bp3-html-select select.bp3-disabled,
  .bp3-select select.bp3-disabled{
    outline:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6); }
    .bp3-html-select select:disabled.bp3-active,
    .bp3-select select:disabled.bp3-active, .bp3-html-select select:disabled.bp3-active:hover,
    .bp3-select select:disabled.bp3-active:hover, .bp3-html-select select.bp3-disabled.bp3-active,
    .bp3-select select.bp3-disabled.bp3-active, .bp3-html-select select.bp3-disabled.bp3-active:hover,
    .bp3-select select.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }

.bp3-html-select.bp3-minimal select,
.bp3-select.bp3-minimal select{
  -webkit-box-shadow:none;
          box-shadow:none;
  background:none; }
  .bp3-html-select.bp3-minimal select:hover,
  .bp3-select.bp3-minimal select:hover{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(167, 182, 194, 0.3);
    text-decoration:none;
    color:#182026; }
  .bp3-html-select.bp3-minimal select:active,
  .bp3-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal select.bp3-active,
  .bp3-select.bp3-minimal select.bp3-active{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:rgba(115, 134, 148, 0.3);
    color:#182026; }
  .bp3-html-select.bp3-minimal select:disabled,
  .bp3-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal select:disabled:hover,
  .bp3-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal select.bp3-disabled,
  .bp3-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal select.bp3-disabled:hover,
  .bp3-select.bp3-minimal select.bp3-disabled:hover{
    background:none;
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6); }
    .bp3-html-select.bp3-minimal select:disabled.bp3-active,
    .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active{
      background:rgba(115, 134, 148, 0.3); }
  .bp3-dark .bp3-html-select.bp3-minimal select, .bp3-html-select.bp3-minimal .bp3-dark select,
  .bp3-dark .bp3-select.bp3-minimal select, .bp3-select.bp3-minimal .bp3-dark select{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:none;
    color:inherit; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover, .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:none; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover{
      background:rgba(138, 155, 168, 0.15); }
    .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:rgba(138, 155, 168, 0.3);
      color:#f5f8fa; }
    .bp3-dark .bp3-html-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal .bp3-dark select:disabled,
    .bp3-dark .bp3-select.bp3-minimal select:disabled, .bp3-select.bp3-minimal .bp3-dark select:disabled, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select:disabled:hover, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover{
      background:none;
      cursor:not-allowed;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-html-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active{
        background:rgba(138, 155, 168, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-primary,
  .bp3-select.bp3-minimal select.bp3-intent-primary{
    color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:none;
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover{
      background:rgba(19, 124, 189, 0.15);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:rgba(19, 124, 189, 0.3);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled{
      background:none;
      color:rgba(16, 107, 163, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active{
        background:rgba(19, 124, 189, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
      stroke:#106ba3; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary{
      color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.2);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(72, 175, 240, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-success,
  .bp3-select.bp3-minimal select.bp3-intent-success{
    color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:none;
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover{
      background:rgba(15, 153, 96, 0.15);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:rgba(15, 153, 96, 0.3);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled{
      background:none;
      color:rgba(13, 128, 80, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active{
        background:rgba(15, 153, 96, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
      stroke:#0d8050; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success{
      color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.2);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(61, 204, 145, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-warning,
  .bp3-select.bp3-minimal select.bp3-intent-warning{
    color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:none;
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover{
      background:rgba(217, 130, 43, 0.15);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:rgba(217, 130, 43, 0.3);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled{
      background:none;
      color:rgba(191, 115, 38, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active{
        background:rgba(217, 130, 43, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
      stroke:#bf7326; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning{
      color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.2);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(255, 179, 102, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-danger,
  .bp3-select.bp3-minimal select.bp3-intent-danger{
    color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      -webkit-box-shadow:none;
              box-shadow:none;
      background:none;
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover{
      background:rgba(219, 55, 55, 0.15);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:rgba(219, 55, 55, 0.3);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled{
      background:none;
      color:rgba(194, 48, 48, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active{
        background:rgba(219, 55, 55, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
      stroke:#c23030; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger{
      color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.2);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(255, 115, 115, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }

.bp3-html-select.bp3-large select,
.bp3-select.bp3-large select{
  height:40px;
  padding-right:35px;
  font-size:16px; }

.bp3-dark .bp3-html-select select, .bp3-dark .bp3-select select{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
  background-color:#394b59;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
  color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover, .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    background-color:#30404d; }
  .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background-color:#202b33;
    background-image:none; }
  .bp3-dark .bp3-html-select select:disabled, .bp3-dark .bp3-select select:disabled, .bp3-dark .bp3-html-select select.bp3-disabled, .bp3-dark .bp3-select select.bp3-disabled{
    -webkit-box-shadow:none;
            box-shadow:none;
    background-color:rgba(57, 75, 89, 0.5);
    background-image:none;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-html-select select:disabled.bp3-active, .bp3-dark .bp3-select select:disabled.bp3-active, .bp3-dark .bp3-html-select select.bp3-disabled.bp3-active, .bp3-dark .bp3-select select.bp3-disabled.bp3-active{
      background:rgba(57, 75, 89, 0.7); }
  .bp3-dark .bp3-html-select select .bp3-button-spinner .bp3-spinner-head, .bp3-dark .bp3-select select .bp3-button-spinner .bp3-spinner-head{
    background:rgba(16, 22, 26, 0.5);
    stroke:#8a9ba8; }

.bp3-html-select select:disabled,
.bp3-select select:disabled{
  -webkit-box-shadow:none;
          box-shadow:none;
  background-color:rgba(206, 217, 224, 0.5);
  cursor:not-allowed;
  color:rgba(92, 112, 128, 0.6); }

.bp3-html-select .bp3-icon,
.bp3-select .bp3-icon, .bp3-select::after{
  position:absolute;
  top:7px;
  right:7px;
  color:#5c7080;
  pointer-events:none; }
  .bp3-html-select .bp3-disabled.bp3-icon,
  .bp3-select .bp3-disabled.bp3-icon, .bp3-disabled.bp3-select::after{
    color:rgba(92, 112, 128, 0.6); }
.bp3-html-select,
.bp3-select{
  display:inline-block;
  position:relative;
  vertical-align:middle;
  letter-spacing:normal; }
  .bp3-html-select select::-ms-expand,
  .bp3-select select::-ms-expand{
    display:none; }
  .bp3-html-select .bp3-icon,
  .bp3-select .bp3-icon{
    color:#5c7080; }
    .bp3-html-select .bp3-icon:hover,
    .bp3-select .bp3-icon:hover{
      color:#182026; }
    .bp3-dark .bp3-html-select .bp3-icon, .bp3-dark
    .bp3-select .bp3-icon{
      color:#a7b6c2; }
      .bp3-dark .bp3-html-select .bp3-icon:hover, .bp3-dark
      .bp3-select .bp3-icon:hover{
        color:#f5f8fa; }
  .bp3-html-select.bp3-large::after,
  .bp3-html-select.bp3-large .bp3-icon,
  .bp3-select.bp3-large::after,
  .bp3-select.bp3-large .bp3-icon{
    top:12px;
    right:12px; }
  .bp3-html-select.bp3-fill,
  .bp3-html-select.bp3-fill select,
  .bp3-select.bp3-fill,
  .bp3-select.bp3-fill select{
    width:100%; }
  .bp3-dark .bp3-html-select option, .bp3-dark
  .bp3-select option{
    background-color:#30404d;
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select::after, .bp3-dark
  .bp3-select::after{
    color:#a7b6c2; }

.bp3-select::after{
  line-height:1;
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-weight:400;
  font-style:normal;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  content:""; }
.bp3-running-text table, table.bp3-html-table{
  border-spacing:0;
  font-size:14px; }
  .bp3-running-text table th, table.bp3-html-table th,
  .bp3-running-text table td,
  table.bp3-html-table td{
    padding:11px;
    vertical-align:top;
    text-align:left; }
  .bp3-running-text table th, table.bp3-html-table th{
    color:#182026;
    font-weight:600; }
  
  .bp3-running-text table td,
  table.bp3-html-table td{
    color:#182026; }
  .bp3-running-text table tbody tr:first-child th, table.bp3-html-table tbody tr:first-child th,
  .bp3-running-text table tbody tr:first-child td,
  table.bp3-html-table tbody tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-running-text table th, .bp3-running-text .bp3-dark table th, .bp3-dark table.bp3-html-table th{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table td, .bp3-running-text .bp3-dark table td, .bp3-dark table.bp3-html-table td{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table tbody tr:first-child th, .bp3-running-text .bp3-dark table tbody tr:first-child th, .bp3-dark table.bp3-html-table tbody tr:first-child th,
  .bp3-dark .bp3-running-text table tbody tr:first-child td,
  .bp3-running-text .bp3-dark table tbody tr:first-child td,
  .bp3-dark table.bp3-html-table tbody tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }

table.bp3-html-table.bp3-html-table-condensed th,
table.bp3-html-table.bp3-html-table-condensed td, table.bp3-html-table.bp3-small th,
table.bp3-html-table.bp3-small td{
  padding-top:6px;
  padding-bottom:6px; }

table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(191, 204, 214, 0.15); }

table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered tbody tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:none;
          box-shadow:none; }
  table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(191, 204, 214, 0.3);
  cursor:pointer; }

table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(191, 204, 214, 0.4); }

.bp3-dark table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(92, 112, 128, 0.15); }

.bp3-dark table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }

.bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15); }

.bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:first-child{
    -webkit-box-shadow:none;
            box-shadow:none; }

.bp3-dark table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(92, 112, 128, 0.3);
  cursor:pointer; }

.bp3-dark table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(92, 112, 128, 0.4); }

.bp3-key-combo{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center; }
  .bp3-key-combo > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-key-combo > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-key-combo::before,
  .bp3-key-combo > *{
    margin-right:5px; }
  .bp3-key-combo:empty::before,
  .bp3-key-combo > :last-child{
    margin-right:0; }

.bp3-hotkey-dialog{
  top:40px;
  padding-bottom:0; }
  .bp3-hotkey-dialog .bp3-dialog-body{
    margin:0;
    padding:0; }
  .bp3-hotkey-dialog .bp3-hotkey-label{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1; }

.bp3-hotkey-column{
  margin:auto;
  max-height:80vh;
  overflow-y:auto;
  padding:30px; }
  .bp3-hotkey-column .bp3-heading{
    margin-bottom:20px; }
    .bp3-hotkey-column .bp3-heading:not(:first-child){
      margin-top:40px; }

.bp3-hotkey{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-pack:justify;
      -ms-flex-pack:justify;
          justify-content:space-between;
  margin-right:0;
  margin-left:0; }
  .bp3-hotkey:not(:last-child){
    margin-bottom:10px; }
.bp3-icon{
  display:inline-block;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  vertical-align:text-bottom; }
  .bp3-icon:not(:empty)::before{
    content:"" !important;
    content:unset !important; }
  .bp3-icon > svg{
    display:block; }
    .bp3-icon > svg:not([fill]){
      fill:currentColor; }

.bp3-icon.bp3-intent-primary, .bp3-icon-standard.bp3-intent-primary, .bp3-icon-large.bp3-intent-primary{
  color:#106ba3; }
  .bp3-dark .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-icon-large.bp3-intent-primary{
    color:#48aff0; }

.bp3-icon.bp3-intent-success, .bp3-icon-standard.bp3-intent-success, .bp3-icon-large.bp3-intent-success{
  color:#0d8050; }
  .bp3-dark .bp3-icon.bp3-intent-success, .bp3-dark .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-icon-large.bp3-intent-success{
    color:#3dcc91; }

.bp3-icon.bp3-intent-warning, .bp3-icon-standard.bp3-intent-warning, .bp3-icon-large.bp3-intent-warning{
  color:#bf7326; }
  .bp3-dark .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-icon-large.bp3-intent-warning{
    color:#ffb366; }

.bp3-icon.bp3-intent-danger, .bp3-icon-standard.bp3-intent-danger, .bp3-icon-large.bp3-intent-danger{
  color:#c23030; }
  .bp3-dark .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-icon-large.bp3-intent-danger{
    color:#ff7373; }

span.bp3-icon-standard{
  line-height:1;
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-weight:400;
  font-style:normal;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon-large{
  line-height:1;
  font-family:"Icons20", sans-serif;
  font-size:20px;
  font-weight:400;
  font-style:normal;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon:empty{
  line-height:1;
  font-family:"Icons20";
  font-size:inherit;
  font-weight:400;
  font-style:normal; }
  span.bp3-icon:empty::before{
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased; }

.bp3-icon-add::before{
  content:""; }

.bp3-icon-add-column-left::before{
  content:""; }

.bp3-icon-add-column-right::before{
  content:""; }

.bp3-icon-add-row-bottom::before{
  content:""; }

.bp3-icon-add-row-top::before{
  content:""; }

.bp3-icon-add-to-artifact::before{
  content:""; }

.bp3-icon-add-to-folder::before{
  content:""; }

.bp3-icon-airplane::before{
  content:""; }

.bp3-icon-align-center::before{
  content:""; }

.bp3-icon-align-justify::before{
  content:""; }

.bp3-icon-align-left::before{
  content:""; }

.bp3-icon-align-right::before{
  content:""; }

.bp3-icon-alignment-bottom::before{
  content:""; }

.bp3-icon-alignment-horizontal-center::before{
  content:""; }

.bp3-icon-alignment-left::before{
  content:""; }

.bp3-icon-alignment-right::before{
  content:""; }

.bp3-icon-alignment-top::before{
  content:""; }

.bp3-icon-alignment-vertical-center::before{
  content:""; }

.bp3-icon-annotation::before{
  content:""; }

.bp3-icon-application::before{
  content:""; }

.bp3-icon-applications::before{
  content:""; }

.bp3-icon-archive::before{
  content:""; }

.bp3-icon-arrow-bottom-left::before{
  content:"↙"; }

.bp3-icon-arrow-bottom-right::before{
  content:"↘"; }

.bp3-icon-arrow-down::before{
  content:"↓"; }

.bp3-icon-arrow-left::before{
  content:"←"; }

.bp3-icon-arrow-right::before{
  content:"→"; }

.bp3-icon-arrow-top-left::before{
  content:"↖"; }

.bp3-icon-arrow-top-right::before{
  content:"↗"; }

.bp3-icon-arrow-up::before{
  content:"↑"; }

.bp3-icon-arrows-horizontal::before{
  content:"↔"; }

.bp3-icon-arrows-vertical::before{
  content:"↕"; }

.bp3-icon-asterisk::before{
  content:"*"; }

.bp3-icon-automatic-updates::before{
  content:""; }

.bp3-icon-badge::before{
  content:""; }

.bp3-icon-ban-circle::before{
  content:""; }

.bp3-icon-bank-account::before{
  content:""; }

.bp3-icon-barcode::before{
  content:""; }

.bp3-icon-blank::before{
  content:""; }

.bp3-icon-blocked-person::before{
  content:""; }

.bp3-icon-bold::before{
  content:""; }

.bp3-icon-book::before{
  content:""; }

.bp3-icon-bookmark::before{
  content:""; }

.bp3-icon-box::before{
  content:""; }

.bp3-icon-briefcase::before{
  content:""; }

.bp3-icon-bring-data::before{
  content:""; }

.bp3-icon-build::before{
  content:""; }

.bp3-icon-calculator::before{
  content:""; }

.bp3-icon-calendar::before{
  content:""; }

.bp3-icon-camera::before{
  content:""; }

.bp3-icon-caret-down::before{
  content:"⌄"; }

.bp3-icon-caret-left::before{
  content:"〈"; }

.bp3-icon-caret-right::before{
  content:"〉"; }

.bp3-icon-caret-up::before{
  content:"⌃"; }

.bp3-icon-cell-tower::before{
  content:""; }

.bp3-icon-changes::before{
  content:""; }

.bp3-icon-chart::before{
  content:""; }

.bp3-icon-chat::before{
  content:""; }

.bp3-icon-chevron-backward::before{
  content:""; }

.bp3-icon-chevron-down::before{
  content:""; }

.bp3-icon-chevron-forward::before{
  content:""; }

.bp3-icon-chevron-left::before{
  content:""; }

.bp3-icon-chevron-right::before{
  content:""; }

.bp3-icon-chevron-up::before{
  content:""; }

.bp3-icon-circle::before{
  content:""; }

.bp3-icon-circle-arrow-down::before{
  content:""; }

.bp3-icon-circle-arrow-left::before{
  content:""; }

.bp3-icon-circle-arrow-right::before{
  content:""; }

.bp3-icon-circle-arrow-up::before{
  content:""; }

.bp3-icon-citation::before{
  content:""; }

.bp3-icon-clean::before{
  content:""; }

.bp3-icon-clipboard::before{
  content:""; }

.bp3-icon-cloud::before{
  content:"☁"; }

.bp3-icon-cloud-download::before{
  content:""; }

.bp3-icon-cloud-upload::before{
  content:""; }

.bp3-icon-code::before{
  content:""; }

.bp3-icon-code-block::before{
  content:""; }

.bp3-icon-cog::before{
  content:""; }

.bp3-icon-collapse-all::before{
  content:""; }

.bp3-icon-column-layout::before{
  content:""; }

.bp3-icon-comment::before{
  content:""; }

.bp3-icon-comparison::before{
  content:""; }

.bp3-icon-compass::before{
  content:""; }

.bp3-icon-compressed::before{
  content:""; }

.bp3-icon-confirm::before{
  content:""; }

.bp3-icon-console::before{
  content:""; }

.bp3-icon-contrast::before{
  content:""; }

.bp3-icon-control::before{
  content:""; }

.bp3-icon-credit-card::before{
  content:""; }

.bp3-icon-cross::before{
  content:"✗"; }

.bp3-icon-crown::before{
  content:""; }

.bp3-icon-cube::before{
  content:""; }

.bp3-icon-cube-add::before{
  content:""; }

.bp3-icon-cube-remove::before{
  content:""; }

.bp3-icon-curved-range-chart::before{
  content:""; }

.bp3-icon-cut::before{
  content:""; }

.bp3-icon-dashboard::before{
  content:""; }

.bp3-icon-data-lineage::before{
  content:""; }

.bp3-icon-database::before{
  content:""; }

.bp3-icon-delete::before{
  content:""; }

.bp3-icon-delta::before{
  content:"Δ"; }

.bp3-icon-derive-column::before{
  content:""; }

.bp3-icon-desktop::before{
  content:""; }

.bp3-icon-diagram-tree::before{
  content:""; }

.bp3-icon-direction-left::before{
  content:""; }

.bp3-icon-direction-right::before{
  content:""; }

.bp3-icon-disable::before{
  content:""; }

.bp3-icon-document::before{
  content:""; }

.bp3-icon-document-open::before{
  content:""; }

.bp3-icon-document-share::before{
  content:""; }

.bp3-icon-dollar::before{
  content:"$"; }

.bp3-icon-dot::before{
  content:"•"; }

.bp3-icon-double-caret-horizontal::before{
  content:""; }

.bp3-icon-double-caret-vertical::before{
  content:""; }

.bp3-icon-double-chevron-down::before{
  content:""; }

.bp3-icon-double-chevron-left::before{
  content:""; }

.bp3-icon-double-chevron-right::before{
  content:""; }

.bp3-icon-double-chevron-up::before{
  content:""; }

.bp3-icon-doughnut-chart::before{
  content:""; }

.bp3-icon-download::before{
  content:""; }

.bp3-icon-drag-handle-horizontal::before{
  content:""; }

.bp3-icon-drag-handle-vertical::before{
  content:""; }

.bp3-icon-draw::before{
  content:""; }

.bp3-icon-drive-time::before{
  content:""; }

.bp3-icon-duplicate::before{
  content:""; }

.bp3-icon-edit::before{
  content:"✎"; }

.bp3-icon-eject::before{
  content:"⏏"; }

.bp3-icon-endorsed::before{
  content:""; }

.bp3-icon-envelope::before{
  content:"✉"; }

.bp3-icon-equals::before{
  content:""; }

.bp3-icon-eraser::before{
  content:""; }

.bp3-icon-error::before{
  content:""; }

.bp3-icon-euro::before{
  content:"€"; }

.bp3-icon-exchange::before{
  content:""; }

.bp3-icon-exclude-row::before{
  content:""; }

.bp3-icon-expand-all::before{
  content:""; }

.bp3-icon-export::before{
  content:""; }

.bp3-icon-eye-off::before{
  content:""; }

.bp3-icon-eye-on::before{
  content:""; }

.bp3-icon-eye-open::before{
  content:""; }

.bp3-icon-fast-backward::before{
  content:""; }

.bp3-icon-fast-forward::before{
  content:""; }

.bp3-icon-feed::before{
  content:""; }

.bp3-icon-feed-subscribed::before{
  content:""; }

.bp3-icon-film::before{
  content:""; }

.bp3-icon-filter::before{
  content:""; }

.bp3-icon-filter-keep::before{
  content:""; }

.bp3-icon-filter-list::before{
  content:""; }

.bp3-icon-filter-open::before{
  content:""; }

.bp3-icon-filter-remove::before{
  content:""; }

.bp3-icon-flag::before{
  content:"⚑"; }

.bp3-icon-flame::before{
  content:""; }

.bp3-icon-flash::before{
  content:""; }

.bp3-icon-floppy-disk::before{
  content:""; }

.bp3-icon-flow-branch::before{
  content:""; }

.bp3-icon-flow-end::before{
  content:""; }

.bp3-icon-flow-linear::before{
  content:""; }

.bp3-icon-flow-review::before{
  content:""; }

.bp3-icon-flow-review-branch::before{
  content:""; }

.bp3-icon-flows::before{
  content:""; }

.bp3-icon-folder-close::before{
  content:""; }

.bp3-icon-folder-new::before{
  content:""; }

.bp3-icon-folder-open::before{
  content:""; }

.bp3-icon-folder-shared::before{
  content:""; }

.bp3-icon-folder-shared-open::before{
  content:""; }

.bp3-icon-follower::before{
  content:""; }

.bp3-icon-following::before{
  content:""; }

.bp3-icon-font::before{
  content:""; }

.bp3-icon-fork::before{
  content:""; }

.bp3-icon-form::before{
  content:""; }

.bp3-icon-full-circle::before{
  content:""; }

.bp3-icon-full-stacked-chart::before{
  content:""; }

.bp3-icon-fullscreen::before{
  content:""; }

.bp3-icon-function::before{
  content:""; }

.bp3-icon-gantt-chart::before{
  content:""; }

.bp3-icon-geolocation::before{
  content:""; }

.bp3-icon-geosearch::before{
  content:""; }

.bp3-icon-git-branch::before{
  content:""; }

.bp3-icon-git-commit::before{
  content:""; }

.bp3-icon-git-merge::before{
  content:""; }

.bp3-icon-git-new-branch::before{
  content:""; }

.bp3-icon-git-pull::before{
  content:""; }

.bp3-icon-git-push::before{
  content:""; }

.bp3-icon-git-repo::before{
  content:""; }

.bp3-icon-glass::before{
  content:""; }

.bp3-icon-globe::before{
  content:""; }

.bp3-icon-globe-network::before{
  content:""; }

.bp3-icon-graph::before{
  content:""; }

.bp3-icon-graph-remove::before{
  content:""; }

.bp3-icon-greater-than::before{
  content:""; }

.bp3-icon-greater-than-or-equal-to::before{
  content:""; }

.bp3-icon-grid::before{
  content:""; }

.bp3-icon-grid-view::before{
  content:""; }

.bp3-icon-group-objects::before{
  content:""; }

.bp3-icon-grouped-bar-chart::before{
  content:""; }

.bp3-icon-hand::before{
  content:""; }

.bp3-icon-hand-down::before{
  content:""; }

.bp3-icon-hand-left::before{
  content:""; }

.bp3-icon-hand-right::before{
  content:""; }

.bp3-icon-hand-up::before{
  content:""; }

.bp3-icon-header::before{
  content:""; }

.bp3-icon-header-one::before{
  content:""; }

.bp3-icon-header-two::before{
  content:""; }

.bp3-icon-headset::before{
  content:""; }

.bp3-icon-heart::before{
  content:"♥"; }

.bp3-icon-heart-broken::before{
  content:""; }

.bp3-icon-heat-grid::before{
  content:""; }

.bp3-icon-heatmap::before{
  content:""; }

.bp3-icon-help::before{
  content:"?"; }

.bp3-icon-helper-management::before{
  content:""; }

.bp3-icon-highlight::before{
  content:""; }

.bp3-icon-history::before{
  content:""; }

.bp3-icon-home::before{
  content:"⌂"; }

.bp3-icon-horizontal-bar-chart::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-asc::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-desc::before{
  content:""; }

.bp3-icon-horizontal-distribution::before{
  content:""; }

.bp3-icon-id-number::before{
  content:""; }

.bp3-icon-image-rotate-left::before{
  content:""; }

.bp3-icon-image-rotate-right::before{
  content:""; }

.bp3-icon-import::before{
  content:""; }

.bp3-icon-inbox::before{
  content:""; }

.bp3-icon-inbox-filtered::before{
  content:""; }

.bp3-icon-inbox-geo::before{
  content:""; }

.bp3-icon-inbox-search::before{
  content:""; }

.bp3-icon-inbox-update::before{
  content:""; }

.bp3-icon-info-sign::before{
  content:"ℹ"; }

.bp3-icon-inheritance::before{
  content:""; }

.bp3-icon-inner-join::before{
  content:""; }

.bp3-icon-insert::before{
  content:""; }

.bp3-icon-intersection::before{
  content:""; }

.bp3-icon-ip-address::before{
  content:""; }

.bp3-icon-issue::before{
  content:""; }

.bp3-icon-issue-closed::before{
  content:""; }

.bp3-icon-issue-new::before{
  content:""; }

.bp3-icon-italic::before{
  content:""; }

.bp3-icon-join-table::before{
  content:""; }

.bp3-icon-key::before{
  content:""; }

.bp3-icon-key-backspace::before{
  content:""; }

.bp3-icon-key-command::before{
  content:""; }

.bp3-icon-key-control::before{
  content:""; }

.bp3-icon-key-delete::before{
  content:""; }

.bp3-icon-key-enter::before{
  content:""; }

.bp3-icon-key-escape::before{
  content:""; }

.bp3-icon-key-option::before{
  content:""; }

.bp3-icon-key-shift::before{
  content:""; }

.bp3-icon-key-tab::before{
  content:""; }

.bp3-icon-known-vehicle::before{
  content:""; }

.bp3-icon-label::before{
  content:""; }

.bp3-icon-layer::before{
  content:""; }

.bp3-icon-layers::before{
  content:""; }

.bp3-icon-layout::before{
  content:""; }

.bp3-icon-layout-auto::before{
  content:""; }

.bp3-icon-layout-balloon::before{
  content:""; }

.bp3-icon-layout-circle::before{
  content:""; }

.bp3-icon-layout-grid::before{
  content:""; }

.bp3-icon-layout-group-by::before{
  content:""; }

.bp3-icon-layout-hierarchy::before{
  content:""; }

.bp3-icon-layout-linear::before{
  content:""; }

.bp3-icon-layout-skew-grid::before{
  content:""; }

.bp3-icon-layout-sorted-clusters::before{
  content:""; }

.bp3-icon-learning::before{
  content:""; }

.bp3-icon-left-join::before{
  content:""; }

.bp3-icon-less-than::before{
  content:""; }

.bp3-icon-less-than-or-equal-to::before{
  content:""; }

.bp3-icon-lifesaver::before{
  content:""; }

.bp3-icon-lightbulb::before{
  content:""; }

.bp3-icon-link::before{
  content:""; }

.bp3-icon-list::before{
  content:"☰"; }

.bp3-icon-list-columns::before{
  content:""; }

.bp3-icon-list-detail-view::before{
  content:""; }

.bp3-icon-locate::before{
  content:""; }

.bp3-icon-lock::before{
  content:""; }

.bp3-icon-log-in::before{
  content:""; }

.bp3-icon-log-out::before{
  content:""; }

.bp3-icon-manual::before{
  content:""; }

.bp3-icon-manually-entered-data::before{
  content:""; }

.bp3-icon-map::before{
  content:""; }

.bp3-icon-map-create::before{
  content:""; }

.bp3-icon-map-marker::before{
  content:""; }

.bp3-icon-maximize::before{
  content:""; }

.bp3-icon-media::before{
  content:""; }

.bp3-icon-menu::before{
  content:""; }

.bp3-icon-menu-closed::before{
  content:""; }

.bp3-icon-menu-open::before{
  content:""; }

.bp3-icon-merge-columns::before{
  content:""; }

.bp3-icon-merge-links::before{
  content:""; }

.bp3-icon-minimize::before{
  content:""; }

.bp3-icon-minus::before{
  content:"−"; }

.bp3-icon-mobile-phone::before{
  content:""; }

.bp3-icon-mobile-video::before{
  content:""; }

.bp3-icon-moon::before{
  content:""; }

.bp3-icon-more::before{
  content:""; }

.bp3-icon-mountain::before{
  content:""; }

.bp3-icon-move::before{
  content:""; }

.bp3-icon-mugshot::before{
  content:""; }

.bp3-icon-multi-select::before{
  content:""; }

.bp3-icon-music::before{
  content:""; }

.bp3-icon-new-drawing::before{
  content:""; }

.bp3-icon-new-grid-item::before{
  content:""; }

.bp3-icon-new-layer::before{
  content:""; }

.bp3-icon-new-layers::before{
  content:""; }

.bp3-icon-new-link::before{
  content:""; }

.bp3-icon-new-object::before{
  content:""; }

.bp3-icon-new-person::before{
  content:""; }

.bp3-icon-new-prescription::before{
  content:""; }

.bp3-icon-new-text-box::before{
  content:""; }

.bp3-icon-ninja::before{
  content:""; }

.bp3-icon-not-equal-to::before{
  content:""; }

.bp3-icon-notifications::before{
  content:""; }

.bp3-icon-notifications-updated::before{
  content:""; }

.bp3-icon-numbered-list::before{
  content:""; }

.bp3-icon-numerical::before{
  content:""; }

.bp3-icon-office::before{
  content:""; }

.bp3-icon-offline::before{
  content:""; }

.bp3-icon-oil-field::before{
  content:""; }

.bp3-icon-one-column::before{
  content:""; }

.bp3-icon-outdated::before{
  content:""; }

.bp3-icon-page-layout::before{
  content:""; }

.bp3-icon-panel-stats::before{
  content:""; }

.bp3-icon-panel-table::before{
  content:""; }

.bp3-icon-paperclip::before{
  content:""; }

.bp3-icon-paragraph::before{
  content:""; }

.bp3-icon-path::before{
  content:""; }

.bp3-icon-path-search::before{
  content:""; }

.bp3-icon-pause::before{
  content:""; }

.bp3-icon-people::before{
  content:""; }

.bp3-icon-percentage::before{
  content:""; }

.bp3-icon-person::before{
  content:""; }

.bp3-icon-phone::before{
  content:"☎"; }

.bp3-icon-pie-chart::before{
  content:""; }

.bp3-icon-pin::before{
  content:""; }

.bp3-icon-pivot::before{
  content:""; }

.bp3-icon-pivot-table::before{
  content:""; }

.bp3-icon-play::before{
  content:""; }

.bp3-icon-plus::before{
  content:"+"; }

.bp3-icon-polygon-filter::before{
  content:""; }

.bp3-icon-power::before{
  content:""; }

.bp3-icon-predictive-analysis::before{
  content:""; }

.bp3-icon-prescription::before{
  content:""; }

.bp3-icon-presentation::before{
  content:""; }

.bp3-icon-print::before{
  content:"⎙"; }

.bp3-icon-projects::before{
  content:""; }

.bp3-icon-properties::before{
  content:""; }

.bp3-icon-property::before{
  content:""; }

.bp3-icon-publish-function::before{
  content:""; }

.bp3-icon-pulse::before{
  content:""; }

.bp3-icon-random::before{
  content:""; }

.bp3-icon-record::before{
  content:""; }

.bp3-icon-redo::before{
  content:""; }

.bp3-icon-refresh::before{
  content:""; }

.bp3-icon-regression-chart::before{
  content:""; }

.bp3-icon-remove::before{
  content:""; }

.bp3-icon-remove-column::before{
  content:""; }

.bp3-icon-remove-column-left::before{
  content:""; }

.bp3-icon-remove-column-right::before{
  content:""; }

.bp3-icon-remove-row-bottom::before{
  content:""; }

.bp3-icon-remove-row-top::before{
  content:""; }

.bp3-icon-repeat::before{
  content:""; }

.bp3-icon-reset::before{
  content:""; }

.bp3-icon-resolve::before{
  content:""; }

.bp3-icon-rig::before{
  content:""; }

.bp3-icon-right-join::before{
  content:""; }

.bp3-icon-ring::before{
  content:""; }

.bp3-icon-rotate-document::before{
  content:""; }

.bp3-icon-rotate-page::before{
  content:""; }

.bp3-icon-satellite::before{
  content:""; }

.bp3-icon-saved::before{
  content:""; }

.bp3-icon-scatter-plot::before{
  content:""; }

.bp3-icon-search::before{
  content:""; }

.bp3-icon-search-around::before{
  content:""; }

.bp3-icon-search-template::before{
  content:""; }

.bp3-icon-search-text::before{
  content:""; }

.bp3-icon-segmented-control::before{
  content:""; }

.bp3-icon-select::before{
  content:""; }

.bp3-icon-selection::before{
  content:"⦿"; }

.bp3-icon-send-to::before{
  content:""; }

.bp3-icon-send-to-graph::before{
  content:""; }

.bp3-icon-send-to-map::before{
  content:""; }

.bp3-icon-series-add::before{
  content:""; }

.bp3-icon-series-configuration::before{
  content:""; }

.bp3-icon-series-derived::before{
  content:""; }

.bp3-icon-series-filtered::before{
  content:""; }

.bp3-icon-series-search::before{
  content:""; }

.bp3-icon-settings::before{
  content:""; }

.bp3-icon-share::before{
  content:""; }

.bp3-icon-shield::before{
  content:""; }

.bp3-icon-shop::before{
  content:""; }

.bp3-icon-shopping-cart::before{
  content:""; }

.bp3-icon-signal-search::before{
  content:""; }

.bp3-icon-sim-card::before{
  content:""; }

.bp3-icon-slash::before{
  content:""; }

.bp3-icon-small-cross::before{
  content:""; }

.bp3-icon-small-minus::before{
  content:""; }

.bp3-icon-small-plus::before{
  content:""; }

.bp3-icon-small-tick::before{
  content:""; }

.bp3-icon-snowflake::before{
  content:""; }

.bp3-icon-social-media::before{
  content:""; }

.bp3-icon-sort::before{
  content:""; }

.bp3-icon-sort-alphabetical::before{
  content:""; }

.bp3-icon-sort-alphabetical-desc::before{
  content:""; }

.bp3-icon-sort-asc::before{
  content:""; }

.bp3-icon-sort-desc::before{
  content:""; }

.bp3-icon-sort-numerical::before{
  content:""; }

.bp3-icon-sort-numerical-desc::before{
  content:""; }

.bp3-icon-split-columns::before{
  content:""; }

.bp3-icon-square::before{
  content:""; }

.bp3-icon-stacked-chart::before{
  content:""; }

.bp3-icon-star::before{
  content:"★"; }

.bp3-icon-star-empty::before{
  content:"☆"; }

.bp3-icon-step-backward::before{
  content:""; }

.bp3-icon-step-chart::before{
  content:""; }

.bp3-icon-step-forward::before{
  content:""; }

.bp3-icon-stop::before{
  content:""; }

.bp3-icon-stopwatch::before{
  content:""; }

.bp3-icon-strikethrough::before{
  content:""; }

.bp3-icon-style::before{
  content:""; }

.bp3-icon-swap-horizontal::before{
  content:""; }

.bp3-icon-swap-vertical::before{
  content:""; }

.bp3-icon-symbol-circle::before{
  content:""; }

.bp3-icon-symbol-cross::before{
  content:""; }

.bp3-icon-symbol-diamond::before{
  content:""; }

.bp3-icon-symbol-square::before{
  content:""; }

.bp3-icon-symbol-triangle-down::before{
  content:""; }

.bp3-icon-symbol-triangle-up::before{
  content:""; }

.bp3-icon-tag::before{
  content:""; }

.bp3-icon-take-action::before{
  content:""; }

.bp3-icon-taxi::before{
  content:""; }

.bp3-icon-text-highlight::before{
  content:""; }

.bp3-icon-th::before{
  content:""; }

.bp3-icon-th-derived::before{
  content:""; }

.bp3-icon-th-disconnect::before{
  content:""; }

.bp3-icon-th-filtered::before{
  content:""; }

.bp3-icon-th-list::before{
  content:""; }

.bp3-icon-thumbs-down::before{
  content:""; }

.bp3-icon-thumbs-up::before{
  content:""; }

.bp3-icon-tick::before{
  content:"✓"; }

.bp3-icon-tick-circle::before{
  content:""; }

.bp3-icon-time::before{
  content:"⏲"; }

.bp3-icon-timeline-area-chart::before{
  content:""; }

.bp3-icon-timeline-bar-chart::before{
  content:""; }

.bp3-icon-timeline-events::before{
  content:""; }

.bp3-icon-timeline-line-chart::before{
  content:""; }

.bp3-icon-tint::before{
  content:""; }

.bp3-icon-torch::before{
  content:""; }

.bp3-icon-tractor::before{
  content:""; }

.bp3-icon-train::before{
  content:""; }

.bp3-icon-translate::before{
  content:""; }

.bp3-icon-trash::before{
  content:""; }

.bp3-icon-tree::before{
  content:""; }

.bp3-icon-trending-down::before{
  content:""; }

.bp3-icon-trending-up::before{
  content:""; }

.bp3-icon-truck::before{
  content:""; }

.bp3-icon-two-columns::before{
  content:""; }

.bp3-icon-unarchive::before{
  content:""; }

.bp3-icon-underline::before{
  content:"⎁"; }

.bp3-icon-undo::before{
  content:"⎌"; }

.bp3-icon-ungroup-objects::before{
  content:""; }

.bp3-icon-unknown-vehicle::before{
  content:""; }

.bp3-icon-unlock::before{
  content:""; }

.bp3-icon-unpin::before{
  content:""; }

.bp3-icon-unresolve::before{
  content:""; }

.bp3-icon-updated::before{
  content:""; }

.bp3-icon-upload::before{
  content:""; }

.bp3-icon-user::before{
  content:""; }

.bp3-icon-variable::before{
  content:""; }

.bp3-icon-vertical-bar-chart-asc::before{
  content:""; }

.bp3-icon-vertical-bar-chart-desc::before{
  content:""; }

.bp3-icon-vertical-distribution::before{
  content:""; }

.bp3-icon-video::before{
  content:""; }

.bp3-icon-volume-down::before{
  content:""; }

.bp3-icon-volume-off::before{
  content:""; }

.bp3-icon-volume-up::before{
  content:""; }

.bp3-icon-walk::before{
  content:""; }

.bp3-icon-warning-sign::before{
  content:""; }

.bp3-icon-waterfall-chart::before{
  content:""; }

.bp3-icon-widget::before{
  content:""; }

.bp3-icon-widget-button::before{
  content:""; }

.bp3-icon-widget-footer::before{
  content:""; }

.bp3-icon-widget-header::before{
  content:""; }

.bp3-icon-wrench::before{
  content:""; }

.bp3-icon-zoom-in::before{
  content:""; }

.bp3-icon-zoom-out::before{
  content:""; }

.bp3-icon-zoom-to-fit::before{
  content:""; }
.bp3-submenu > .bp3-popover-wrapper{
  display:block; }

.bp3-submenu .bp3-popover-target{
  display:block; }

.bp3-submenu.bp3-popover{
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0 5px; }
  .bp3-submenu.bp3-popover > .bp3-popover-content{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-submenu.bp3-popover, .bp3-submenu.bp3-popover.bp3-dark{
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-dark .bp3-submenu.bp3-popover > .bp3-popover-content, .bp3-submenu.bp3-popover.bp3-dark > .bp3-popover-content{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
.bp3-menu{
  margin:0;
  border-radius:3px;
  background:#ffffff;
  min-width:180px;
  padding:5px;
  list-style:none;
  text-align:left;
  color:#182026; }

.bp3-menu-divider{
  display:block;
  margin:5px;
  border-top:1px solid rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-menu-divider{
    border-top-color:rgba(255, 255, 255, 0.15); }

.bp3-menu-item{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  border-radius:2px;
  padding:5px 7px;
  text-decoration:none;
  line-height:20px;
  color:inherit;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-menu-item > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-menu-item > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-menu-item::before,
  .bp3-menu-item > *{
    margin-right:7px; }
  .bp3-menu-item:empty::before,
  .bp3-menu-item > :last-child{
    margin-right:0; }
  .bp3-menu-item > .bp3-fill{
    word-break:break-word; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    background-color:rgba(167, 182, 194, 0.3);
    cursor:pointer;
    text-decoration:none; }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit;
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-dark .bp3-menu-item{
    color:inherit; }
    .bp3-dark .bp3-menu-item:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
      background-color:rgba(138, 155, 168, 0.15);
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-disabled{
      background-color:inherit;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-menu-item.bp3-intent-primary{
    color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-primary::before, .bp3-menu-item.bp3-intent-primary::after,
    .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary:active, .bp3-menu-item.bp3-intent-primary:active::before, .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-success{
    color:#0d8050; }
    .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-success::before, .bp3-menu-item.bp3-intent-success::after,
    .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-menu-item.bp3-intent-success:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success:active, .bp3-menu-item.bp3-intent-success:active::before, .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-warning{
    color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-warning::before, .bp3-menu-item.bp3-intent-warning::after,
    .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning:active, .bp3-menu-item.bp3-intent-warning:active::before, .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-danger{
    color:#c23030; }
    .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-danger::before, .bp3-menu-item.bp3-intent-danger::after,
    .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger:active, .bp3-menu-item.bp3-intent-danger:active::before, .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item::before{
    line-height:1;
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-weight:400;
    font-style:normal;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    margin-right:7px; }
  .bp3-menu-item::before,
  .bp3-menu-item > .bp3-icon{
    margin-top:2px;
    color:#5c7080; }
  .bp3-menu-item .bp3-menu-item-label{
    color:#5c7080; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    color:inherit; }
  .bp3-menu-item.bp3-active, .bp3-menu-item:active{
    background-color:rgba(115, 134, 148, 0.3); }
  .bp3-menu-item.bp3-disabled{
    outline:none !important;
    background-color:inherit !important;
    cursor:not-allowed !important;
    color:rgba(92, 112, 128, 0.6) !important; }
    .bp3-menu-item.bp3-disabled::before,
    .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-large .bp3-menu-item{
    padding:9px 7px;
    line-height:22px;
    font-size:16px; }
    .bp3-large .bp3-menu-item .bp3-icon{
      margin-top:3px; }
    .bp3-large .bp3-menu-item::before{
      line-height:1;
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-weight:400;
      font-style:normal;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      margin-top:1px;
      margin-right:10px; }

button.bp3-menu-item{
  border:none;
  background:none;
  width:100%;
  text-align:left; }
.bp3-menu-header{
  display:block;
  margin:5px;
  border-top:1px solid rgba(16, 22, 26, 0.15);
  cursor:default;
  padding-left:2px; }
  .bp3-dark .bp3-menu-header{
    border-top-color:rgba(255, 255, 255, 0.15); }
  .bp3-menu-header:first-of-type{
    border-top:none; }
  .bp3-menu-header > h6{
    color:#182026;
    font-weight:600;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    margin:0;
    padding:10px 7px 0 1px;
    line-height:17px; }
    .bp3-dark .bp3-menu-header > h6{
      color:#f5f8fa; }
  .bp3-menu-header:first-of-type > h6{
    padding-top:0; }
  .bp3-large .bp3-menu-header > h6{
    padding-top:15px;
    padding-bottom:5px;
    font-size:18px; }
  .bp3-large .bp3-menu-header:first-of-type > h6{
    padding-top:0; }

.bp3-dark .bp3-menu{
  background:#30404d;
  color:#f5f8fa; }

.bp3-dark .bp3-menu-item.bp3-intent-primary{
  color:#48aff0; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary::before, .bp3-dark .bp3-menu-item.bp3-intent-primary::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
    color:#48aff0; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active{
    background-color:#137cbd; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary:active{
    background-color:#106ba3; }
  .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary:active, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item.bp3-intent-success{
  color:#3dcc91; }
  .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-success::before, .bp3-dark .bp3-menu-item.bp3-intent-success::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
    color:#3dcc91; }
  .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active{
    background-color:#0f9960; }
  .bp3-dark .bp3-menu-item.bp3-intent-success:active{
    background-color:#0d8050; }
  .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success:active, .bp3-dark .bp3-menu-item.bp3-intent-success:active::before, .bp3-dark .bp3-menu-item.bp3-intent-success:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item.bp3-intent-warning{
  color:#ffb366; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning::before, .bp3-dark .bp3-menu-item.bp3-intent-warning::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
    color:#ffb366; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active{
    background-color:#d9822b; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning:active{
    background-color:#bf7326; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning:active, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item.bp3-intent-danger{
  color:#ff7373; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-icon{
    color:inherit; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger::before, .bp3-dark .bp3-menu-item.bp3-intent-danger::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
    color:#ff7373; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active{
    background-color:#db3737; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger:active{
    background-color:#c23030; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
  .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label,
  .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger:active, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::after,
  .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
    color:#ffffff; }

.bp3-dark .bp3-menu-item::before,
.bp3-dark .bp3-menu-item > .bp3-icon{
  color:#a7b6c2; }

.bp3-dark .bp3-menu-item .bp3-menu-item-label{
  color:#a7b6c2; }

.bp3-dark .bp3-menu-item.bp3-active, .bp3-dark .bp3-menu-item:active{
  background-color:rgba(138, 155, 168, 0.3); }

.bp3-dark .bp3-menu-item.bp3-disabled{
  color:rgba(167, 182, 194, 0.6) !important; }
  .bp3-dark .bp3-menu-item.bp3-disabled::before,
  .bp3-dark .bp3-menu-item.bp3-disabled > .bp3-icon,
  .bp3-dark .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
    color:rgba(167, 182, 194, 0.6) !important; }

.bp3-dark .bp3-menu-divider,
.bp3-dark .bp3-menu-header{
  border-color:rgba(255, 255, 255, 0.15); }

.bp3-dark .bp3-menu-header > h6{
  color:#f5f8fa; }

.bp3-label .bp3-menu{
  margin-top:5px; }
.bp3-navbar{
  position:relative;
  z-index:10;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  background-color:#ffffff;
  width:100%;
  height:50px;
  padding:0 15px; }
  .bp3-navbar.bp3-dark,
  .bp3-dark .bp3-navbar{
    background-color:#394b59; }
  .bp3-navbar.bp3-dark{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-navbar{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-navbar.bp3-fixed-top{
    position:fixed;
    top:0;
    right:0;
    left:0; }

.bp3-navbar-heading{
  margin-right:15px;
  font-size:16px; }

.bp3-navbar-group{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  height:50px; }
  .bp3-navbar-group.bp3-align-left{
    float:left; }
  .bp3-navbar-group.bp3-align-right{
    float:right; }

.bp3-navbar-divider{
  margin:0 10px;
  border-left:1px solid rgba(16, 22, 26, 0.15);
  height:20px; }
  .bp3-dark .bp3-navbar-divider{
    border-left-color:rgba(255, 255, 255, 0.15); }
.bp3-non-ideal-state{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  width:100%;
  height:100%;
  text-align:center; }
  .bp3-non-ideal-state > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-non-ideal-state > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-non-ideal-state::before,
  .bp3-non-ideal-state > *{
    margin-bottom:20px; }
  .bp3-non-ideal-state:empty::before,
  .bp3-non-ideal-state > :last-child{
    margin-bottom:0; }
  .bp3-non-ideal-state > *{
    max-width:400px; }

.bp3-non-ideal-state-visual{
  color:rgba(92, 112, 128, 0.6);
  font-size:60px; }
  .bp3-dark .bp3-non-ideal-state-visual{
    color:rgba(167, 182, 194, 0.6); }

.bp3-overflow-list{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:nowrap;
      flex-wrap:nowrap;
  min-width:0; }

.bp3-overflow-list-spacer{
  -ms-flex-negative:1;
      flex-shrink:1;
  width:1px; }

body.bp3-overlay-open{
  overflow:hidden; }

.bp3-overlay{
  position:static;
  top:0;
  right:0;
  bottom:0;
  left:0;
  z-index:20; }
  .bp3-overlay:not(.bp3-overlay-open){
    pointer-events:none; }
  .bp3-overlay.bp3-overlay-container{
    position:fixed;
    overflow:hidden; }
    .bp3-overlay.bp3-overlay-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-scroll-container{
    position:fixed;
    overflow:auto; }
    .bp3-overlay.bp3-overlay-scroll-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-inline{
    display:inline;
    overflow:visible; }

.bp3-overlay-content{
  position:fixed;
  z-index:20; }
  .bp3-overlay-inline .bp3-overlay-content,
  .bp3-overlay-scroll-container .bp3-overlay-content{
    position:absolute; }

.bp3-overlay-backdrop{
  position:fixed;
  top:0;
  right:0;
  bottom:0;
  left:0;
  opacity:1;
  z-index:20;
  background-color:rgba(16, 22, 26, 0.7);
  overflow:auto;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-overlay-backdrop.bp3-overlay-enter, .bp3-overlay-backdrop.bp3-overlay-appear{
    opacity:0; }
  .bp3-overlay-backdrop.bp3-overlay-enter-active, .bp3-overlay-backdrop.bp3-overlay-appear-active{
    opacity:1;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-overlay-backdrop.bp3-overlay-exit{
    opacity:1; }
  .bp3-overlay-backdrop.bp3-overlay-exit-active{
    opacity:0;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-overlay-backdrop:focus{
    outline:none; }
  .bp3-overlay-inline .bp3-overlay-backdrop{
    position:absolute; }
.bp3-panel-stack{
  position:relative;
  overflow:hidden; }

.bp3-panel-stack-header{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  z-index:1;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  height:30px; }
  .bp3-dark .bp3-panel-stack-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack-header > span{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1;
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch; }
  .bp3-panel-stack-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack-view{
  position:absolute;
  top:0;
  right:0;
  bottom:0;
  left:0;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  background-color:#ffffff;
  overflow-y:auto; }
  .bp3-dark .bp3-panel-stack-view{
    background-color:#30404d; }

.bp3-panel-stack-push .bp3-panel-stack-enter, .bp3-panel-stack-push .bp3-panel-stack-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack-push .bp3-panel-stack-enter-active, .bp3-panel-stack-push .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease;
  -webkit-transition-delay:0;
          transition-delay:0; }

.bp3-panel-stack-push .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-push .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease;
  -webkit-transition-delay:0;
          transition-delay:0; }

.bp3-panel-stack-pop .bp3-panel-stack-enter, .bp3-panel-stack-pop .bp3-panel-stack-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack-pop .bp3-panel-stack-enter-active, .bp3-panel-stack-pop .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease;
  -webkit-transition-delay:0;
          transition-delay:0; }

.bp3-panel-stack-pop .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-pop .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease;
  -webkit-transition-delay:0;
          transition-delay:0; }
.bp3-popover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1);
  display:inline-block;
  z-index:20;
  border-radius:3px; }
  .bp3-popover .bp3-popover-arrow{
    position:absolute;
    width:30px;
    height:30px; }
    .bp3-popover .bp3-popover-arrow::before{
      margin:5px;
      width:20px;
      height:20px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover{
    margin-top:-17px;
    margin-bottom:17px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
      bottom:-11px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover{
    margin-left:17px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
      left:-11px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover{
    margin-top:17px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
      top:-11px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover{
    margin-right:17px;
    margin-left:-17px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
      right:-11px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-popover > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-popover > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
    top:-0.3934px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
    right:-0.3934px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
    left:-0.3934px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
    bottom:-0.3934px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-popover .bp3-popover-content{
    background:#ffffff;
    color:inherit; }
  .bp3-popover .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-popover .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-popover .bp3-popover-arrow-fill{
    fill:#ffffff; }
  .bp3-popover-enter > .bp3-popover, .bp3-popover-appear > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3); }
  .bp3-popover-enter-active > .bp3-popover, .bp3-popover-appear-active > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-popover-exit > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3);
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-popover .bp3-popover-content{
    position:relative;
    border-radius:3px; }
  .bp3-popover.bp3-popover-content-sizing .bp3-popover-content{
    max-width:350px;
    padding:20px; }
  .bp3-popover-target + .bp3-overlay .bp3-popover.bp3-popover-content-sizing{
    width:350px; }
  .bp3-popover.bp3-minimal{
    margin:0 !important; }
    .bp3-popover.bp3-minimal .bp3-popover-arrow{
      display:none; }
    .bp3-popover.bp3-minimal.bp3-popover{
      -webkit-transform:scale(1);
              transform:scale(1); }
      .bp3-popover-enter > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-enter-active > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
        -webkit-transition-delay:0;
                transition-delay:0; }
      .bp3-popover-exit > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-exit-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
        -webkit-transition-delay:0;
                transition-delay:0; }
  .bp3-popover.bp3-dark,
  .bp3-dark .bp3-popover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-popover .bp3-popover-content{
      background:#30404d;
      color:inherit; }
    .bp3-popover.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-popover .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-popover .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-popover.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-popover .bp3-popover-arrow-fill{
      fill:#30404d; }

.bp3-popover-arrow::before{
  display:block;
  position:absolute;
  -webkit-transform:rotate(45deg);
          transform:rotate(45deg);
  border-radius:2px;
  content:""; }

.bp3-tether-pinned .bp3-popover-arrow{
  display:none; }

.bp3-popover-backdrop{
  background:rgba(255, 255, 255, 0); }

.bp3-transition-container{
  opacity:1;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  z-index:20; }
  .bp3-transition-container.bp3-popover-enter, .bp3-transition-container.bp3-popover-appear{
    opacity:0; }
  .bp3-transition-container.bp3-popover-enter-active, .bp3-transition-container.bp3-popover-appear-active{
    opacity:1;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-transition-container.bp3-popover-exit{
    opacity:1; }
  .bp3-transition-container.bp3-popover-exit-active{
    opacity:0;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-transition-container:focus{
    outline:none; }
  .bp3-transition-container.bp3-popover-leave .bp3-popover-content{
    pointer-events:none; }
  .bp3-transition-container[data-x-out-of-boundaries]{
    display:none; }

span.bp3-popover-target{
  display:inline-block; }

.bp3-popover-wrapper.bp3-fill{
  width:100%; }

.bp3-portal{
  position:absolute;
  top:0;
  right:0;
  left:0; }
@-webkit-keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }
@keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }

.bp3-progress-bar{
  display:block;
  position:relative;
  border-radius:40px;
  background:rgba(92, 112, 128, 0.2);
  width:100%;
  height:8px;
  overflow:hidden; }
  .bp3-progress-bar .bp3-progress-meter{
    position:absolute;
    border-radius:40px;
    background:linear-gradient(-45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%);
    background-color:rgba(92, 112, 128, 0.8);
    background-size:30px 30px;
    width:100%;
    height:100%;
    -webkit-transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-progress-bar:not(.bp3-no-animation):not(.bp3-no-stripes) .bp3-progress-meter{
    animation:linear-progress-bar-stripes 300ms linear infinite reverse; }
  .bp3-progress-bar.bp3-no-stripes .bp3-progress-meter{
    background-image:none; }

.bp3-dark .bp3-progress-bar{
  background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-progress-bar .bp3-progress-meter{
    background-color:#8a9ba8; }

.bp3-progress-bar.bp3-intent-primary .bp3-progress-meter{
  background-color:#137cbd; }

.bp3-progress-bar.bp3-intent-success .bp3-progress-meter{
  background-color:#0f9960; }

.bp3-progress-bar.bp3-intent-warning .bp3-progress-meter{
  background-color:#d9822b; }

.bp3-progress-bar.bp3-intent-danger .bp3-progress-meter{
  background-color:#db3737; }
@-webkit-keyframes skeleton-glow{
  from{
    border-color:rgba(206, 217, 224, 0.2);
    background:rgba(206, 217, 224, 0.2); }
  to{
    border-color:rgba(92, 112, 128, 0.2);
    background:rgba(92, 112, 128, 0.2); } }
@keyframes skeleton-glow{
  from{
    border-color:rgba(206, 217, 224, 0.2);
    background:rgba(206, 217, 224, 0.2); }
  to{
    border-color:rgba(92, 112, 128, 0.2);
    background:rgba(92, 112, 128, 0.2); } }
.bp3-skeleton{
  border-color:rgba(206, 217, 224, 0.2) !important;
  border-radius:2px;
  -webkit-box-shadow:none !important;
          box-shadow:none !important;
  background:rgba(206, 217, 224, 0.2);
  background-clip:padding-box !important;
  cursor:default;
  color:transparent !important;
  -webkit-animation:1000ms linear infinite alternate skeleton-glow;
          animation:1000ms linear infinite alternate skeleton-glow;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-skeleton::before, .bp3-skeleton::after,
  .bp3-skeleton *{
    visibility:hidden !important; }
.bp3-slider{
  width:100%;
  min-width:150px;
  height:40px;
  position:relative;
  outline:none;
  cursor:default;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-slider:hover{
    cursor:pointer; }
  .bp3-slider:active{
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-slider.bp3-disabled{
    opacity:0.5;
    cursor:not-allowed; }
  .bp3-slider.bp3-slider-unlabeled{
    height:16px; }

.bp3-slider-track,
.bp3-slider-progress{
  top:5px;
  right:0;
  left:0;
  height:6px;
  position:absolute; }

.bp3-slider-track{
  border-radius:3px;
  overflow:hidden; }

.bp3-slider-progress{
  background:rgba(92, 112, 128, 0.2); }
  .bp3-dark .bp3-slider-progress{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-slider-progress.bp3-intent-primary{
    background-color:#137cbd; }
  .bp3-slider-progress.bp3-intent-success{
    background-color:#0f9960; }
  .bp3-slider-progress.bp3-intent-warning{
    background-color:#d9822b; }
  .bp3-slider-progress.bp3-intent-danger{
    background-color:#db3737; }

.bp3-slider-handle{
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  color:#182026;
  position:absolute;
  top:0;
  left:0;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
  cursor:pointer;
  width:16px;
  height:16px; }
  .bp3-slider-handle:hover{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    background-clip:padding-box;
    background-color:#ebf1f5; }
  .bp3-slider-handle:active, .bp3-slider-handle.bp3-active{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background-color:#d8e1e8;
    background-image:none; }
  .bp3-slider-handle:disabled, .bp3-slider-handle.bp3-disabled{
    outline:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6); }
    .bp3-slider-handle:disabled.bp3-active, .bp3-slider-handle:disabled.bp3-active:hover, .bp3-slider-handle.bp3-disabled.bp3-active, .bp3-slider-handle.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }
  .bp3-slider-handle:focus{
    z-index:1; }
  .bp3-slider-handle:hover{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    background-clip:padding-box;
    background-color:#ebf1f5;
    z-index:2;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
    cursor:-webkit-grab;
    cursor:grab; }
  .bp3-slider-handle.bp3-active{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-disabled .bp3-slider-handle{
    -webkit-box-shadow:none;
            box-shadow:none;
    background:#bfccd6;
    pointer-events:none; }
  .bp3-dark .bp3-slider-handle{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover, .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      background-color:#30404d; }
    .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
      background-color:#202b33;
      background-image:none; }
    .bp3-dark .bp3-slider-handle:disabled, .bp3-dark .bp3-slider-handle.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none;
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-slider-handle:disabled.bp3-active, .bp3-dark .bp3-slider-handle.bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-slider-handle .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-slider-handle, .bp3-dark .bp3-slider-handle:hover{
      background-color:#394b59; }
    .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#293742; }
  .bp3-dark .bp3-disabled .bp3-slider-handle{
    border-color:#5c7080;
    -webkit-box-shadow:none;
            box-shadow:none;
    background:#5c7080; }
  .bp3-slider-handle .bp3-slider-label{
    margin-left:8px;
    border-radius:3px;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
    background:#394b59;
    color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle .bp3-slider-label{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
      background:#e1e8ed;
      color:#394b59; }
    .bp3-disabled .bp3-slider-handle .bp3-slider-label{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-slider-handle.bp3-start, .bp3-slider-handle.bp3-end{
    width:8px; }
  .bp3-slider-handle.bp3-start{
    border-top-right-radius:0;
    border-bottom-right-radius:0; }
  .bp3-slider-handle.bp3-end{
    margin-left:8px;
    border-top-left-radius:0;
    border-bottom-left-radius:0; }
    .bp3-slider-handle.bp3-end .bp3-slider-label{
      margin-left:0; }

.bp3-slider-label{
  -webkit-transform:translate(-50%, 20px);
          transform:translate(-50%, 20px);
  display:inline-block;
  position:absolute;
  padding:2px 5px;
  vertical-align:top;
  line-height:1;
  font-size:12px; }

.bp3-slider.bp3-vertical{
  width:40px;
  min-width:40px;
  height:150px; }
  .bp3-slider.bp3-vertical .bp3-slider-track,
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    top:0;
    bottom:0;
    left:5px;
    width:6px;
    height:auto; }
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    top:auto; }
  .bp3-slider.bp3-vertical .bp3-slider-label{
    -webkit-transform:translate(20px, 50%);
            transform:translate(20px, 50%); }
  .bp3-slider.bp3-vertical .bp3-slider-handle{
    top:auto; }
    .bp3-slider.bp3-vertical .bp3-slider-handle .bp3-slider-label{
      margin-top:-8px;
      margin-left:0; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end, .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      margin-left:0;
      width:16px;
      height:8px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      border-top-left-radius:0;
      border-bottom-right-radius:3px; }
      .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start .bp3-slider-label{
        -webkit-transform:translate(20px);
                transform:translate(20px); }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end{
      margin-bottom:8px;
      border-top-left-radius:3px;
      border-bottom-left-radius:0;
      border-bottom-right-radius:0; }

@-webkit-keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

@keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

.bp3-spinner{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  overflow:visible;
  vertical-align:middle; }
  .bp3-spinner svg{
    display:block; }
  .bp3-spinner path{
    fill-opacity:0; }
  .bp3-spinner .bp3-spinner-head{
    -webkit-transform-origin:center;
            transform-origin:center;
    -webkit-transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    stroke:rgba(92, 112, 128, 0.8);
    stroke-linecap:round; }
  .bp3-spinner .bp3-spinner-track{
    stroke:rgba(92, 112, 128, 0.2); }

.bp3-spinner-animation{
  -webkit-animation:pt-spinner-animation 500ms linear infinite;
          animation:pt-spinner-animation 500ms linear infinite; }
  .bp3-no-spin > .bp3-spinner-animation{
    -webkit-animation:none;
            animation:none; }

.bp3-dark .bp3-spinner .bp3-spinner-head{
  stroke:#8a9ba8; }

.bp3-dark .bp3-spinner .bp3-spinner-track{
  stroke:rgba(16, 22, 26, 0.5); }

.bp3-spinner.bp3-intent-primary .bp3-spinner-head{
  stroke:#137cbd; }

.bp3-spinner.bp3-intent-success .bp3-spinner-head{
  stroke:#0f9960; }

.bp3-spinner.bp3-intent-warning .bp3-spinner-head{
  stroke:#d9822b; }

.bp3-spinner.bp3-intent-danger .bp3-spinner-head{
  stroke:#db3737; }
.bp3-tabs.bp3-vertical{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-tabs.bp3-vertical > .bp3-tab-list{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column;
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab{
      border-radius:3px;
      width:100%;
      padding:0 10px; }
      .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab[aria-selected="true"]{
        -webkit-box-shadow:none;
                box-shadow:none;
        background-color:rgba(19, 124, 189, 0.2); }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab-indicator-wrapper .bp3-tab-indicator{
      top:0;
      right:0;
      bottom:0;
      left:0;
      border-radius:3px;
      background-color:rgba(19, 124, 189, 0.2);
      height:auto; }
  .bp3-tabs.bp3-vertical > .bp3-tab-panel{
    margin-top:0;
    padding-left:20px; }

.bp3-tab-list{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  -webkit-box-align:end;
      -ms-flex-align:end;
          align-items:flex-end;
  position:relative;
  margin:0;
  border:none;
  padding:0;
  list-style:none; }
  .bp3-tab-list > *:not(:last-child){
    margin-right:20px; }

.bp3-tab{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  position:relative;
  cursor:pointer;
  max-width:100%;
  vertical-align:top;
  line-height:30px;
  color:#182026;
  font-size:14px; }
  .bp3-tab a{
    display:block;
    text-decoration:none;
    color:inherit; }
  .bp3-tab-indicator-wrapper ~ .bp3-tab{
    -webkit-box-shadow:none !important;
            box-shadow:none !important;
    background-color:transparent !important; }
  .bp3-tab[aria-disabled="true"]{
    cursor:not-allowed;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-tab[aria-selected="true"]{
    border-radius:0;
    -webkit-box-shadow:inset 0 -3px 0 #106ba3;
            box-shadow:inset 0 -3px 0 #106ba3; }
  .bp3-tab[aria-selected="true"], .bp3-tab:not([aria-disabled="true"]):hover{
    color:#106ba3; }
  .bp3-tab:focus{
    -moz-outline-radius:0; }
  .bp3-large > .bp3-tab{
    line-height:40px;
    font-size:16px; }

.bp3-tab-panel{
  margin-top:20px; }
  .bp3-tab-panel[aria-hidden="true"]{
    display:none; }

.bp3-tab-indicator-wrapper{
  position:absolute;
  top:0;
  left:0;
  -webkit-transform:translateX(0), translateY(0);
          transform:translateX(0), translateY(0);
  -webkit-transition:height, width, -webkit-transform;
  transition:height, width, -webkit-transform;
  transition:height, transform, width;
  transition:height, transform, width, -webkit-transform;
  -webkit-transition-duration:200ms;
          transition-duration:200ms;
  -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
          transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
  pointer-events:none; }
  .bp3-tab-indicator-wrapper .bp3-tab-indicator{
    position:absolute;
    right:0;
    bottom:0;
    left:0;
    background-color:#106ba3;
    height:3px; }
  .bp3-tab-indicator-wrapper.bp3-no-animation{
    -webkit-transition:none;
    transition:none; }

.bp3-dark .bp3-tab{
  color:#f5f8fa; }
  .bp3-dark .bp3-tab[aria-disabled="true"]{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tab[aria-selected="true"]{
    -webkit-box-shadow:inset 0 -3px 0 #48aff0;
            box-shadow:inset 0 -3px 0 #48aff0; }
  .bp3-dark .bp3-tab[aria-selected="true"], .bp3-dark .bp3-tab:not([aria-disabled="true"]):hover{
    color:#48aff0; }

.bp3-dark .bp3-tab-indicator{
  background-color:#48aff0; }

.bp3-flex-expander{
  -webkit-box-flex:1;
      -ms-flex:1 1;
          flex:1 1; }
.bp3-tag{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  position:relative;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:none;
          box-shadow:none;
  background-color:#5c7080;
  min-width:20px;
  max-width:100%;
  min-height:20px;
  padding:2px 6px;
  line-height:16px;
  color:#f5f8fa;
  font-size:12px; }
  .bp3-tag.bp3-interactive{
    cursor:pointer; }
    .bp3-tag.bp3-interactive:hover{
      background-color:rgba(92, 112, 128, 0.85); }
    .bp3-tag.bp3-interactive.bp3-active, .bp3-tag.bp3-interactive:active{
      background-color:rgba(92, 112, 128, 0.7); }
  .bp3-tag > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag::before,
  .bp3-tag > *{
    margin-right:4px; }
  .bp3-tag:empty::before,
  .bp3-tag > :last-child{
    margin-right:0; }
  .bp3-tag:focus{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:0;
    -moz-outline-radius:6px; }
  .bp3-tag.bp3-round{
    border-radius:30px;
    padding-right:8px;
    padding-left:8px; }
  .bp3-dark .bp3-tag{
    background-color:#bfccd6;
    color:#182026; }
    .bp3-dark .bp3-tag.bp3-interactive{
      cursor:pointer; }
      .bp3-dark .bp3-tag.bp3-interactive:hover{
        background-color:rgba(191, 204, 214, 0.85); }
      .bp3-dark .bp3-tag.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-interactive:active{
        background-color:rgba(191, 204, 214, 0.7); }
    .bp3-dark .bp3-tag > .bp3-icon, .bp3-dark .bp3-tag .bp3-icon-standard, .bp3-dark .bp3-tag .bp3-icon-large{
      fill:currentColor; }
  .bp3-tag > .bp3-icon, .bp3-tag .bp3-icon-standard, .bp3-tag .bp3-icon-large{
    fill:#ffffff; }
  .bp3-tag.bp3-large,
  .bp3-large .bp3-tag{
    min-width:30px;
    min-height:30px;
    padding:0 10px;
    line-height:20px;
    font-size:14px; }
    .bp3-tag.bp3-large::before,
    .bp3-tag.bp3-large > *,
    .bp3-large .bp3-tag::before,
    .bp3-large .bp3-tag > *{
      margin-right:7px; }
    .bp3-tag.bp3-large:empty::before,
    .bp3-tag.bp3-large > :last-child,
    .bp3-large .bp3-tag:empty::before,
    .bp3-large .bp3-tag > :last-child{
      margin-right:0; }
    .bp3-tag.bp3-large.bp3-round,
    .bp3-large .bp3-tag.bp3-round{
      padding-right:12px;
      padding-left:12px; }
  .bp3-tag.bp3-intent-primary{
    background:#137cbd;
    color:#ffffff; }
    .bp3-tag.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.85); }
      .bp3-tag.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.7); }
  .bp3-tag.bp3-intent-success{
    background:#0f9960;
    color:#ffffff; }
    .bp3-tag.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.85); }
      .bp3-tag.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.7); }
  .bp3-tag.bp3-intent-warning{
    background:#d9822b;
    color:#ffffff; }
    .bp3-tag.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.85); }
      .bp3-tag.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.7); }
  .bp3-tag.bp3-intent-danger{
    background:#db3737;
    color:#ffffff; }
    .bp3-tag.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.85); }
      .bp3-tag.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.7); }
  .bp3-tag.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-tag.bp3-minimal > .bp3-icon, .bp3-tag.bp3-minimal .bp3-icon-standard, .bp3-tag.bp3-minimal .bp3-icon-large{
    fill:#5c7080; }
  .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
    background-color:rgba(138, 155, 168, 0.2);
    color:#182026; }
    .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
        background-color:rgba(92, 112, 128, 0.3); }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
        background-color:rgba(92, 112, 128, 0.4); }
    .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
      color:#f5f8fa; }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
          background-color:rgba(191, 204, 214, 0.3); }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
          background-color:rgba(191, 204, 214, 0.4); }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) > .bp3-icon, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-large{
        fill:#a7b6c2; }
  .bp3-tag.bp3-minimal.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15);
    color:#106ba3; }
    .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-primary > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-large{
      fill:#137cbd; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25);
      color:#48aff0; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
          background-color:rgba(19, 124, 189, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
          background-color:rgba(19, 124, 189, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15);
    color:#0d8050; }
    .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-success > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-large{
      fill:#0f9960; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25);
      color:#3dcc91; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
          background-color:rgba(15, 153, 96, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
          background-color:rgba(15, 153, 96, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15);
    color:#bf7326; }
    .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-warning > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-large{
      fill:#d9822b; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25);
      color:#ffb366; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
          background-color:rgba(217, 130, 43, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
          background-color:rgba(217, 130, 43, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15);
    color:#c23030; }
    .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-danger > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-large{
      fill:#db3737; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25);
      color:#ff7373; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
          background-color:rgba(219, 55, 55, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
          background-color:rgba(219, 55, 55, 0.45); }

.bp3-tag-remove{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  opacity:0.5;
  margin-top:-2px;
  margin-right:-6px !important;
  margin-bottom:-2px;
  border:none;
  background:none;
  cursor:pointer;
  padding:2px;
  padding-left:0;
  color:inherit; }
  .bp3-tag-remove:hover{
    opacity:0.8;
    background:none;
    text-decoration:none; }
  .bp3-tag-remove:active{
    opacity:1; }
  .bp3-tag-remove:empty::before{
    line-height:1;
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-weight:400;
    font-style:normal;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    content:""; }
  .bp3-large .bp3-tag-remove{
    margin-right:-10px !important;
    padding:5px;
    padding-left:0; }
    .bp3-large .bp3-tag-remove:empty::before{
      line-height:1;
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-weight:400;
      font-style:normal; }
.bp3-tag-input{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  cursor:text;
  height:auto;
  min-height:30px;
  padding-right:0;
  padding-left:5px;
  line-height:inherit; }
  .bp3-tag-input > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag-input > .bp3-tag-input-values{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag-input .bp3-tag-input-icon{
    margin-top:7px;
    margin-right:7px;
    margin-left:2px;
    color:#5c7080; }
  .bp3-tag-input .bp3-tag-input-values{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row;
    -ms-flex-wrap:wrap;
        flex-wrap:wrap;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    -ms-flex-item-align:stretch;
        align-self:stretch;
    margin-top:5px;
    margin-right:7px;
    min-width:0; }
    .bp3-tag-input .bp3-tag-input-values > *{
      -webkit-box-flex:0;
          -ms-flex-positive:0;
              flex-grow:0;
      -ms-flex-negative:0;
          flex-shrink:0; }
    .bp3-tag-input .bp3-tag-input-values > .bp3-fill{
      -webkit-box-flex:1;
          -ms-flex-positive:1;
              flex-grow:1;
      -ms-flex-negative:1;
          flex-shrink:1; }
    .bp3-tag-input .bp3-tag-input-values::before,
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-right:5px; }
    .bp3-tag-input .bp3-tag-input-values:empty::before,
    .bp3-tag-input .bp3-tag-input-values > :last-child{
      margin-right:0; }
    .bp3-tag-input .bp3-tag-input-values:first-child .bp3-input-ghost:first-child{
      padding-left:5px; }
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-bottom:5px; }
  .bp3-tag-input .bp3-tag{
    overflow-wrap:break-word; }
    .bp3-tag-input .bp3-tag.bp3-active{
      outline:rgba(19, 124, 189, 0.6) auto 2px;
      outline-offset:0;
      -moz-outline-radius:6px; }
  .bp3-tag-input .bp3-input-ghost{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:80px;
    line-height:20px; }
    .bp3-tag-input .bp3-input-ghost:disabled, .bp3-tag-input .bp3-input-ghost.bp3-disabled{
      cursor:not-allowed; }
  .bp3-tag-input .bp3-button,
  .bp3-tag-input .bp3-spinner{
    margin:3px;
    margin-left:0; }
  .bp3-tag-input .bp3-button{
    min-width:24px;
    min-height:24px;
    padding:0 7px; }
  .bp3-tag-input.bp3-large{
    height:auto;
    min-height:40px; }
    .bp3-tag-input.bp3-large::before,
    .bp3-tag-input.bp3-large > *{
      margin-right:10px; }
    .bp3-tag-input.bp3-large:empty::before,
    .bp3-tag-input.bp3-large > :last-child{
      margin-right:0; }
    .bp3-tag-input.bp3-large .bp3-tag-input-icon{
      margin-top:10px;
      margin-left:5px; }
    .bp3-tag-input.bp3-large .bp3-input-ghost{
      line-height:30px; }
    .bp3-tag-input.bp3-large .bp3-button{
      min-width:30px;
      min-height:30px;
      padding:5px 10px;
      margin:5px;
      margin-left:0; }
    .bp3-tag-input.bp3-large .bp3-spinner{
      margin:8px;
      margin-left:0; }
  .bp3-tag-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
    background-color:#ffffff; }
    .bp3-tag-input.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-tag-input .bp3-tag-input-icon, .bp3-tag-input.bp3-dark .bp3-tag-input-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-tag-input .bp3-input-ghost, .bp3-tag-input.bp3-dark .bp3-input-ghost{
    color:#f5f8fa; }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-webkit-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-moz-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost:-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::placeholder{
      color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tag-input.bp3-active, .bp3-tag-input.bp3-dark.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    background-color:rgba(16, 22, 26, 0.3); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-primary, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-success, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-warning, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-danger, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-input-ghost{
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  background:none;
  padding:0; }
  .bp3-input-ghost::-webkit-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input-ghost::-moz-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input-ghost:-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input-ghost::-ms-input-placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input-ghost::placeholder{
    opacity:1;
    color:rgba(92, 112, 128, 0.6); }
  .bp3-input-ghost:focus{
    outline:none !important; }
.bp3-toast{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  position:relative !important;
  margin:20px 0 0;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  background-color:#ffffff;
  min-width:300px;
  max-width:500px;
  pointer-events:all; }
  .bp3-toast.bp3-toast-enter, .bp3-toast.bp3-toast-appear{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active, .bp3-toast.bp3-toast-appear-active{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-toast.bp3-toast-enter ~ .bp3-toast, .bp3-toast.bp3-toast-appear ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active ~ .bp3-toast, .bp3-toast.bp3-toast-appear-active ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-toast.bp3-toast-exit{
    opacity:1;
    -webkit-filter:blur(0);
            filter:blur(0); }
  .bp3-toast.bp3-toast-exit-active{
    opacity:0;
    -webkit-filter:blur(10px);
            filter:blur(10px);
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:opacity, filter;
    transition-property:opacity, filter, -webkit-filter;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-toast.bp3-toast-exit ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0); }
  .bp3-toast.bp3-toast-exit-active ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px);
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:50ms;
            transition-delay:50ms; }
  .bp3-toast .bp3-button-group{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    padding:5px;
    padding-left:0; }
  .bp3-toast > .bp3-icon{
    margin:12px;
    margin-right:0;
    color:#5c7080; }
  .bp3-toast.bp3-dark,
  .bp3-dark .bp3-toast{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
    background-color:#394b59; }
    .bp3-toast.bp3-dark > .bp3-icon,
    .bp3-dark .bp3-toast > .bp3-icon{
      color:#a7b6c2; }
  .bp3-toast[class*="bp3-intent-"] a{
    color:rgba(255, 255, 255, 0.7); }
    .bp3-toast[class*="bp3-intent-"] a:hover{
      color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] > .bp3-icon{
    color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button, .bp3-toast[class*="bp3-intent-"] .bp3-button::before,
  .bp3-toast[class*="bp3-intent-"] .bp3-button .bp3-icon, .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    color:rgba(255, 255, 255, 0.7) !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:focus{
    outline-color:rgba(255, 255, 255, 0.5); }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:hover{
    background-color:rgba(255, 255, 255, 0.15) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    background-color:rgba(255, 255, 255, 0.3) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button::after{
    background:rgba(255, 255, 255, 0.3) !important; }
  .bp3-toast.bp3-intent-primary{
    background-color:#137cbd;
    color:#ffffff; }
  .bp3-toast.bp3-intent-success{
    background-color:#0f9960;
    color:#ffffff; }
  .bp3-toast.bp3-intent-warning{
    background-color:#d9822b;
    color:#ffffff; }
  .bp3-toast.bp3-intent-danger{
    background-color:#db3737;
    color:#ffffff; }

.bp3-toast-message{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  padding:11px;
  word-break:break-word; }

.bp3-toast-container{
  display:-webkit-box !important;
  display:-ms-flexbox !important;
  display:flex !important;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  position:fixed;
  right:0;
  left:0;
  z-index:40;
  overflow:hidden;
  padding:0 20px 20px;
  pointer-events:none; }
  .bp3-toast-container.bp3-toast-container-top{
    top:0;
    bottom:auto; }
  .bp3-toast-container.bp3-toast-container-bottom{
    -webkit-box-orient:vertical;
    -webkit-box-direction:reverse;
        -ms-flex-direction:column-reverse;
            flex-direction:column-reverse;
    top:auto;
    bottom:0; }
  .bp3-toast-container.bp3-toast-container-left{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
  .bp3-toast-container.bp3-toast-container-right{
    -webkit-box-align:end;
        -ms-flex-align:end;
            align-items:flex-end; }

.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active) ~ .bp3-toast, .bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active) ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-leave-active ~ .bp3-toast{
  -webkit-transform:translateY(60px);
          transform:translateY(60px); }
.bp3-tooltip{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1); }
  .bp3-tooltip .bp3-popover-arrow{
    position:absolute;
    width:22px;
    height:22px; }
    .bp3-tooltip .bp3-popover-arrow::before{
      margin:4px;
      width:14px;
      height:14px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip{
    margin-top:-11px;
    margin-bottom:11px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
      bottom:-8px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip{
    margin-left:11px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
      left:-8px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip{
    margin-top:11px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
      top:-8px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip{
    margin-right:11px;
    margin-left:-11px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
      right:-8px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-tooltip > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-tooltip > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
    top:-0.22183px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
    right:-0.22183px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
    left:-0.22183px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
    bottom:-0.22183px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-tooltip .bp3-popover-content{
    background:#394b59;
    color:#f5f8fa; }
  .bp3-tooltip .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-tooltip .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-tooltip .bp3-popover-arrow-fill{
    fill:#394b59; }
  .bp3-popover-enter > .bp3-tooltip, .bp3-popover-appear > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8); }
  .bp3-popover-enter-active > .bp3-tooltip, .bp3-popover-appear-active > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-popover-exit > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8);
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-tooltip .bp3-popover-content{
    padding:10px 12px; }
  .bp3-tooltip.bp3-dark,
  .bp3-dark .bp3-tooltip{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-tooltip .bp3-popover-content{
      background:#e1e8ed;
      color:#394b59; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-fill{
      fill:#e1e8ed; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-content{
    background:#137cbd;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-arrow-fill{
    fill:#137cbd; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-content{
    background:#0f9960;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-arrow-fill{
    fill:#0f9960; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-content{
    background:#d9822b;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-arrow-fill{
    fill:#d9822b; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-content{
    background:#db3737;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-arrow-fill{
    fill:#db3737; }

.bp3-tooltip-indicator{
  border-bottom:dotted 1px;
  cursor:help; }
.bp3-tree .bp3-icon, .bp3-tree .bp3-icon-standard, .bp3-tree .bp3-icon-large{
  color:#5c7080; }
  .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-tree .bp3-icon.bp3-intent-success, .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-tree-node-list{
  margin:0;
  padding-left:0;
  list-style:none; }

.bp3-tree-root{
  position:relative;
  background-color:transparent;
  cursor:default;
  padding-left:0; }

.bp3-tree-node-content-0{
  padding-left:0px; }

.bp3-tree-node-content-1{
  padding-left:23px; }

.bp3-tree-node-content-2{
  padding-left:46px; }

.bp3-tree-node-content-3{
  padding-left:69px; }

.bp3-tree-node-content-4{
  padding-left:92px; }

.bp3-tree-node-content-5{
  padding-left:115px; }

.bp3-tree-node-content-6{
  padding-left:138px; }

.bp3-tree-node-content-7{
  padding-left:161px; }

.bp3-tree-node-content-8{
  padding-left:184px; }

.bp3-tree-node-content-9{
  padding-left:207px; }

.bp3-tree-node-content-10{
  padding-left:230px; }

.bp3-tree-node-content-11{
  padding-left:253px; }

.bp3-tree-node-content-12{
  padding-left:276px; }

.bp3-tree-node-content-13{
  padding-left:299px; }

.bp3-tree-node-content-14{
  padding-left:322px; }

.bp3-tree-node-content-15{
  padding-left:345px; }

.bp3-tree-node-content-16{
  padding-left:368px; }

.bp3-tree-node-content-17{
  padding-left:391px; }

.bp3-tree-node-content-18{
  padding-left:414px; }

.bp3-tree-node-content-19{
  padding-left:437px; }

.bp3-tree-node-content-20{
  padding-left:460px; }

.bp3-tree-node-content{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  width:100%;
  height:30px;
  padding-right:5px; }
  .bp3-tree-node-content:hover{
    background-color:rgba(191, 204, 214, 0.4); }

.bp3-tree-node-caret,
.bp3-tree-node-caret-none{
  min-width:30px; }

.bp3-tree-node-caret{
  color:#5c7080;
  -webkit-transform:rotate(0deg);
          transform:rotate(0deg);
  cursor:pointer;
  padding:7px;
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tree-node-caret:hover{
    color:#182026; }
  .bp3-dark .bp3-tree-node-caret{
    color:#a7b6c2; }
    .bp3-dark .bp3-tree-node-caret:hover{
      color:#f5f8fa; }
  .bp3-tree-node-caret.bp3-tree-node-caret-open{
    -webkit-transform:rotate(90deg);
            transform:rotate(90deg); }
  .bp3-tree-node-caret.bp3-icon-standard::before{
    content:""; }

.bp3-tree-node-icon{
  position:relative;
  margin-right:7px; }

.bp3-tree-node-label{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-label span{
    display:inline; }

.bp3-tree-node-secondary-label{
  padding:0 5px;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-secondary-label .bp3-popover-wrapper,
  .bp3-tree-node-secondary-label .bp3-popover-target{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-content{
  background-color:inherit;
  cursor:not-allowed;
  color:rgba(92, 112, 128, 0.6); }

.bp3-tree-node.bp3-disabled .bp3-tree-node-caret,
.bp3-tree-node.bp3-disabled .bp3-tree-node-icon{
  cursor:not-allowed;
  color:rgba(92, 112, 128, 0.6); }

.bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content,
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-standard, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-large{
    color:#ffffff; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret::before{
    color:rgba(255, 255, 255, 0.7); }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret:hover::before{
    color:#ffffff; }

.bp3-dark .bp3-tree-node-content:hover{
  background-color:rgba(92, 112, 128, 0.3); }

.bp3-dark .bp3-tree .bp3-icon, .bp3-dark .bp3-tree .bp3-icon-standard, .bp3-dark .bp3-tree .bp3-icon-large{
  color:#a7b6c2; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-dark .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
/*!

Copyright 2017-present Palantir Technologies, Inc. All rights reserved.
Licensed under the Apache License, Version 2.0.

*/
.bp3-omnibar{
  -webkit-filter:blur(0);
          filter:blur(0);
  opacity:1;
  top:20vh;
  left:calc(50% - 250px);
  z-index:21;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  background-color:#ffffff;
  width:500px; }
  .bp3-omnibar.bp3-overlay-enter, .bp3-omnibar.bp3-overlay-appear{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2; }
  .bp3-omnibar.bp3-overlay-enter-active, .bp3-omnibar.bp3-overlay-appear-active{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-omnibar.bp3-overlay-exit{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1; }
  .bp3-omnibar.bp3-overlay-exit-active{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
    -webkit-transition-delay:0;
            transition-delay:0; }
  .bp3-omnibar .bp3-input{
    border-radius:0;
    background-color:transparent; }
    .bp3-omnibar .bp3-input, .bp3-omnibar .bp3-input:focus{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-omnibar .bp3-menu{
    border-radius:0;
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
    background-color:transparent;
    max-height:calc(60vh - 40px);
    overflow:auto; }
    .bp3-omnibar .bp3-menu:empty{
      display:none; }
  .bp3-dark .bp3-omnibar, .bp3-omnibar.bp3-dark{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    background-color:#30404d; }

.bp3-omnibar-overlay .bp3-overlay-backdrop{
  background-color:rgba(16, 22, 26, 0.2); }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-width:400px;
  max-height:300px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }

.bp3-multi-select{
  min-width:150px; }

.bp3-multi-select-popover .bp3-menu{
  max-width:400px;
  max-height:300px;
  overflow:auto; }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-width:400px;
  max-height:300px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDhoLTIuODFjLS40NS0uNzgtMS4wNy0xLjQ1LTEuODItMS45NkwxNyA0LjQxIDE1LjU5IDNsLTIuMTcgMi4xN0MxMi45NiA1LjA2IDEyLjQ5IDUgMTIgNWMtLjQ5IDAtLjk2LjA2LTEuNDEuMTdMOC40MSAzIDcgNC40MWwxLjYyIDEuNjNDNy44OCA2LjU1IDcuMjYgNy4yMiA2LjgxIDhINHYyaDIuMDljLS4wNS4zMy0uMDkuNjYtLjA5IDF2MUg0djJoMnYxYzAgLjM0LjA0LjY3LjA5IDFINHYyaDIuODFjMS4wNCAxLjc5IDIuOTcgMyA1LjE5IDNzNC4xNS0xLjIxIDUuMTktM0gyMHYtMmgtMi4wOWMuMDUtLjMzLjA5LS42Ni4wOS0xdi0xaDJ2LTJoLTJ2LTFjMC0uMzQtLjA0LS42Ny0uMDktMUgyMFY4em0tNiA4aC00di0yaDR2MnptMC00aC00di0yaDR2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTYuMTdMNC44MyAxMmwtMS40MiAxLjQxTDkgMTkgMjEgN2wtMS40MS0xLjQxeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1pY29uLWJyYW5kMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNmZmYiPgogICAgPHBhdGggZD0iTTEwNSAxMjcuM2g0MHYxMi44aC00MHpNNTEuMSA3N0w3NCA5OS45bC0yMy4zIDIzLjMgMTAuNSAxMC41IDIzLjMtMjMuM0w5NSA5OS45IDg0LjUgODkuNCA2MS42IDY2LjV6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNGOUE4MjUiPgogICAgPHBhdGggZD0iTTIwLjIgMTEuOGMtMS42IDAtMS43LjUtMS43IDEgMCAuNC4xLjkuMSAxLjMuMS41LjEuOS4xIDEuMyAwIDEuNy0xLjQgMi4zLTMuNSAyLjNoLS45di0xLjloLjVjMS4xIDAgMS40IDAgMS40LS44IDAtLjMgMC0uNi0uMS0xIDAtLjQtLjEtLjgtLjEtMS4yIDAtMS4zIDAtMS44IDEuMy0yLTEuMy0uMi0xLjMtLjctMS4zLTIgMC0uNC4xLS44LjEtMS4yLjEtLjQuMS0uNy4xLTEgMC0uOC0uNC0uNy0xLjQtLjhoLS41VjQuMWguOWMyLjIgMCAzLjUuNyAzLjUgMi4zIDAgLjQtLjEuOS0uMSAxLjMtLjEuNS0uMS45LS4xIDEuMyAwIC41LjIgMSAxLjcgMXYxLjh6TTEuOCAxMC4xYzEuNiAwIDEuNy0uNSAxLjctMSAwLS40LS4xLS45LS4xLTEuMy0uMS0uNS0uMS0uOS0uMS0xLjMgMC0xLjYgMS40LTIuMyAzLjUtMi4zaC45djEuOWgtLjVjLTEgMC0xLjQgMC0xLjQuOCAwIC4zIDAgLjYuMSAxIDAgLjIuMS42LjEgMSAwIDEuMyAwIDEuOC0xLjMgMkM2IDExLjIgNiAxMS43IDYgMTNjMCAuNC0uMS44LS4xIDEuMi0uMS4zLS4xLjctLjEgMSAwIC44LjMuOCAxLjQuOGguNXYxLjloLS45Yy0yLjEgMC0zLjUtLjYtMy41LTIuMyAwLS40LjEtLjkuMS0xLjMuMS0uNS4xLS45LjEtMS4zIDAtLjUtLjItMS0xLjctMXYtMS45eiIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSIxMy44IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY3g9IjExIiBjeT0iOC4yIiByPSIyLjEiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgPGcgY2xhc3M9ImpwLWljb24td2FybjAiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4=);
  --jp-icon-listings-info: url(data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPHN2ZyB2ZXJzaW9uPSIxLjEiIGlkPSJDYXBhXzEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHg9IjBweCIgeT0iMHB4Ig0KCSB2aWV3Qm94PSIwIDAgNTAuOTc4IDUwLjk3OCIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNTAuOTc4IDUwLjk3ODsiIHhtbDpzcGFjZT0icHJlc2VydmUiPg0KPGc+DQoJPGc+DQoJCTxnPg0KCQkJPHBhdGggc3R5bGU9ImZpbGw6IzAxMDAwMjsiIGQ9Ik00My41Miw3LjQ1OEMzOC43MTEsMi42NDgsMzIuMzA3LDAsMjUuNDg5LDBDMTguNjcsMCwxMi4yNjYsMi42NDgsNy40NTgsNy40NTgNCgkJCQljLTkuOTQzLDkuOTQxLTkuOTQzLDI2LjExOSwwLDM2LjA2MmM0LjgwOSw0LjgwOSwxMS4yMTIsNy40NTYsMTguMDMxLDcuNDU4YzAsMCwwLjAwMSwwLDAuMDAyLDANCgkJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoNCgkJCQkgTTQyLjEwNiw0Mi4xMDVjLTQuNDMyLDQuNDMxLTEwLjMzMiw2Ljg3Mi0xNi42MTUsNi44NzJoLTAuMDAyYy02LjI4NS0wLjAwMS0xMi4xODctMi40NDEtMTYuNjE3LTYuODcyDQoJCQkJYy05LjE2Mi05LjE2My05LjE2Mi0yNC4wNzEsMC0zMy4yMzNDMTMuMzAzLDQuNDQsMTkuMjA0LDIsMjUuNDg5LDJjNi4yODQsMCwxMi4xODYsMi40NCwxNi42MTcsNi44NzINCgkJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4NCgkJPC9nPg0KCQk8Zz4NCgkJCTxwYXRoIHN0eWxlPSJmaWxsOiMwMTAwMDI7IiBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1Mw0KCQkJCWMwLjQ2OC0wLjUzNiwwLjkyMy0xLjA2MiwxLjM2Ny0xLjU3NWMwLjYyNi0wLjc1MywxLjEwNC0xLjQ3OCwxLjQzNi0yLjE3NWMwLjMzMS0wLjcwNywwLjQ5NS0xLjU0MSwwLjQ5NS0yLjUNCgkJCQljMC0xLjA5Ni0wLjI2LTIuMDg4LTAuNzc5LTIuOTc5Yy0wLjU2NS0wLjg3OS0xLjUwMS0xLjMzNi0yLjgwNi0xLjM2OWMtMS44MDIsMC4wNTctMi45ODUsMC42NjctMy41NSwxLjgzMg0KCQkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkNCgkJCQljMS4wNjItMS42NCwyLjg1NS0yLjQ4MSw1LjM3OC0yLjUyN2MyLjE2LDAuMDIzLDMuODc0LDAuNjA4LDUuMTQxLDEuNzU4YzEuMjc4LDEuMTYsMS45MjksMi43NjQsMS45NSw0LjgxMQ0KCQkJCWMwLDEuMTQyLTAuMTM3LDIuMTExLTAuNDEsMi45MTFjLTAuMzA5LDAuODQ1LTAuNzMxLDEuNTkzLTEuMjY4LDIuMjQzYy0wLjQ5MiwwLjY1LTEuMDY4LDEuMzE4LTEuNzMsMi4wMDINCgkJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5DQoJCQkJQzI2LjU4OSwzMi4yMTgsMjMuNTc4LDMyLjIxOCwyMy41NzgsMzIuMjE4eiBNMjMuNTc4LDM4LjIydi0zLjQ4NGgzLjA3NnYzLjQ4NEgyMy41Nzh6Ii8+DQoJCTwvZz4NCgk8L2c+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8L3N2Zz4NCg==);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMEQ0N0ExIj4KICAgIDxwYXRoIGQ9Ik0xMS4xIDYuOVY1LjhINi45YzAtLjUgMC0xLjMuMi0xLjYuNC0uNy44LTEuMSAxLjctMS40IDEuNy0uMyAyLjUtLjMgMy45LS4xIDEgLjEgMS45LjkgMS45IDEuOXY0LjJjMCAuNS0uOSAxLjYtMiAxLjZIOC44Yy0xLjUgMC0yLjQgMS40LTIuNCAyLjh2Mi4ySDQuN0MzLjUgMTUuMSAzIDE0IDMgMTMuMVY5Yy0uMS0xIC42LTIgMS44LTIgMS41LS4xIDYuMy0uMSA2LjMtLjF6Ii8+CiAgICA8cGF0aCBkPSJNMTAuOSAxNS4xdjEuMWg0LjJjMCAuNSAwIDEuMy0uMiAxLjYtLjQuNy0uOCAxLjEtMS43IDEuNC0xLjcuMy0yLjUuMy0zLjkuMS0xLS4xLTEuOS0uOS0xLjktMS45di00LjJjMC0uNS45LTEuNiAyLTEuNmgzLjhjMS41IDAgMi40LTEuNCAyLjQtMi44VjYuNmgxLjdDMTguNSA2LjkgMTkgOCAxOSA4LjlWMTNjMCAxLS43IDIuMS0xLjkgMi4xaC02LjJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMikiIGZpbGw9IiMzMzMzMzMiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uLWFjY2VudDIganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGQ9Ik01LjA1NjY0IDguNzYxNzJDNS4wNTY2NCA4LjU5NzY2IDUuMDMxMjUgOC40NTMxMiA0Ljk4MDQ3IDguMzI4MTJDNC45MzM1OSA4LjE5OTIyIDQuODU1NDcgOC4wODIwMyA0Ljc0NjA5IDcuOTc2NTZDNC42NDA2MiA3Ljg3MTA5IDQuNSA3Ljc3NTM5IDQuMzI0MjIgNy42ODk0NUM0LjE1MjM0IDcuNTk5NjEgMy45NDMzNiA3LjUxMTcyIDMuNjk3MjcgNy40MjU3OEMzLjMwMjczIDcuMjg1MTYgMi45NDMzNiA3LjEzNjcyIDIuNjE5MTQgNi45ODA0N0MyLjI5NDkyIDYuODI0MjIgMi4wMTc1OCA2LjY0MjU4IDEuNzg3MTEgNi40MzU1NUMxLjU2MDU1IDYuMjI4NTIgMS4zODQ3NyA1Ljk4ODI4IDEuMjU5NzcgNS43MTQ4NEMxLjEzNDc3IDUuNDM3NSAxLjA3MjI3IDUuMTA5MzggMS4wNzIyNyA0LjczMDQ3QzEuMDcyMjcgNC4zOTg0NCAxLjEyODkxIDQuMDk1NyAxLjI0MjE5IDMuODIyMjdDMS4zNTU0NyAzLjU0NDkyIDEuNTE1NjIgMy4zMDQ2OSAxLjcyMjY2IDMuMTAxNTZDMS45Mjk2OSAyLjg5ODQ0IDIuMTc5NjkgMi43MzQzNyAyLjQ3MjY2IDIuNjA5MzhDMi43NjU2MiAyLjQ4NDM4IDMuMDkxOCAyLjQwNDMgMy40NTExNyAyLjM2OTE0VjEuMTA5MzhINC4zODg2N1YyLjM4MDg2QzQuNzQwMjMgMi40Mjc3MyA1LjA1NjY0IDIuNTIzNDQgNS4zMzc4OSAyLjY2Nzk3QzUuNjE5MTQgMi44MTI1IDUuODU3NDIgMy4wMDE5NSA2LjA1MjczIDMuMjM2MzNDNi4yNTE5NSAzLjQ2NjggNi40MDQzIDMuNzQwMjMgNi41MDk3NyA0LjA1NjY0QzYuNjE5MTQgNC4zNjkxNCA2LjY3MzgzIDQuNzIwNyA2LjY3MzgzIDUuMTExMzNINS4wNDQ5MkM1LjA0NDkyIDQuNjM4NjcgNC45Mzc1IDQuMjgxMjUgNC43MjI2NiA0LjAzOTA2QzQuNTA3ODEgMy43OTI5NyA0LjIxNjggMy42Njk5MiAzLjg0OTYxIDMuNjY5OTJDMy42NTAzOSAzLjY2OTkyIDMuNDc2NTYgMy42OTcyNyAzLjMyODEyIDMuNzUxOTVDMy4xODM1OSAzLjgwMjczIDMuMDY0NDUgMy44NzY5NSAyLjk3MDcgMy45NzQ2MUMyLjg3Njk1IDQuMDY4MzYgMi44MDY2NCA0LjE3OTY5IDIuNzU5NzcgNC4zMDg1OUMyLjcxNjggNC40Mzc1IDIuNjk1MzEgNC41NzgxMiAyLjY5NTMxIDQuNzMwNDdDMi42OTUzMSA0Ljg4MjgxIDIuNzE2OCA1LjAxOTUzIDIuNzU5NzcgNS4xNDA2MkMyLjgwNjY0IDUuMjU3ODEgMi44ODI4MSA1LjM2NzE5IDIuOTg4MjggNS40Njg3NUMzLjA5NzY2IDUuNTcwMzEgMy4yNDAyMyA1LjY2Nzk3IDMuNDE2MDIgNS43NjE3MkMzLjU5MTggNS44NTE1NiAzLjgxMDU1IDUuOTQzMzYgNC4wNzIyNyA2LjAzNzExQzQuNDY2OCA2LjE4NTU1IDQuODI0MjIgNi4zMzk4NCA1LjE0NDUzIDYuNUM1LjQ2NDg0IDYuNjU2MjUgNS43MzgyOCA2LjgzOTg0IDUuOTY0ODQgNy4wNTA3OEM2LjE5NTMxIDcuMjU3ODEgNi4zNzEwOSA3LjUgNi40OTIxOSA3Ljc3NzM0QzYuNjE3MTkgOC4wNTA3OCA2LjY3OTY5IDguMzc1IDYuNjc5NjkgOC43NUM2LjY3OTY5IDkuMDkzNzUgNi42MjMwNSA5LjQwNDMgNi41MDk3NyA5LjY4MTY0QzYuMzk2NDggOS45NTUwOCA2LjIzNDM4IDEwLjE5MTQgNi4wMjM0NCAxMC4zOTA2QzUuODEyNSAxMC41ODk4IDUuNTU4NTkgMTAuNzUgNS4yNjE3MiAxMC44NzExQzQuOTY0ODQgMTAuOTg4MyA0LjYzMjgxIDExLjA2NDUgNC4yNjU2MiAxMS4wOTk2VjEyLjI0OEgzLjMzMzk4VjExLjA5OTZDMy4wMDE5NSAxMS4wNjg0IDIuNjc5NjkgMTAuOTk2MSAyLjM2NzE5IDEwLjg4MjhDMi4wNTQ2OSAxMC43NjU2IDEuNzc3MzQgMTAuNTk3NyAxLjUzNTE2IDEwLjM3ODlDMS4yOTY4OCAxMC4xNjAyIDEuMTA1NDcgOS44ODQ3NyAwLjk2MDkzOCA5LjU1MjczQzAuODE2NDA2IDkuMjE2OCAwLjc0NDE0MSA4LjgxNDQ1IDAuNzQ0MTQxIDguMzQ1N0gyLjM3ODkxQzIuMzc4OTEgOC42MjY5NSAyLjQxOTkyIDguODYzMjggMi41MDE5NSA5LjA1NDY5QzIuNTgzOTggOS4yNDIxOSAyLjY4OTQ1IDkuMzkyNTggMi44MTgzNiA5LjUwNTg2QzIuOTUxMTcgOS42MTUyMyAzLjEwMTU2IDkuNjkzMzYgMy4yNjk1MyA5Ljc0MDIzQzMuNDM3NSA5Ljc4NzExIDMuNjA5MzggOS44MTA1NSAzLjc4NTE2IDkuODEwNTVDNC4yMDMxMiA5LjgxMDU1IDQuNTE5NTMgOS43MTI4OSA0LjczNDM4IDkuNTE3NThDNC45NDkyMiA5LjMyMjI3IDUuMDU2NjQgOS4wNzAzMSA1LjA1NjY0IDguNzYxNzJaTTEzLjQxOCAxMi4yNzE1SDguMDc0MjJWMTFIMTMuNDE4VjEyLjI3MTVaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzLjk1MjY0IDYpIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTUgMTVIM3YyaDEydi0yem0wLThIM3YyaDEyVjd6TTMgMTNoMTh2LTJIM3Yyem0wIDhoMTh2LTJIM3Yyek0zIDN2MmgxOFYzSDN6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}
.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}
.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}
.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}
.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}
.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}
.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}
.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}
.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}
.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}
.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}
.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}
.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}
.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}
.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}
.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}
.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}
.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}
.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}
.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}
.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}
.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}
.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}
.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}
.jp-FileIcon {
  background-image: var(--jp-icon-file);
}
.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}
.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}
.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}
.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}
.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}
.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}
.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}
.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}
.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}
.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}
.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}
.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}
.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}
.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}
.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}
.jp-ListIcon {
  background-image: var(--jp-icon-list);
}
.jp-ListingsInfoIcon {
  background-image: var(--jp-icon-listings-info);
}
.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}
.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}
.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}
.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}
.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}
.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}
.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}
.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}
.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}
.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}
.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}
.jp-RunIcon {
  background-image: var(--jp-icon-run);
}
.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}
.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}
.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}
.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}
.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}
.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}
.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}
.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}
.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}
.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}
.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}
.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}
.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

:root {
  --jp-icon-search-white: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
}

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}
/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}
/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}
.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}
.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}
.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}
.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}
.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}
.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}
.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}
.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}
/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}
.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}
.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}
.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}
.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}
.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}
.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}
/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

/* CSS for icons in selected items in the settings editor */
#setting-editor .jp-PluginList .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
#setting-editor
  .jp-PluginList
  .jp-mod-selected
  .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected tabs in the sidebar tab manager */
#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable[fill] {
  fill: #fff;
}

#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable[fill] {
  fill: var(--jp-brand-color1);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable-inverse[fill] {
  fill: #fff;
}

/**
 * TODO: come up with non css-hack solution for showing the busy icon on top
 *  of the close icon
 * CSS for complex behavior of close icon of tabs in the sidebar tab manager
 */
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-dirty.jp-mod-active
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: #fff;
}

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) svg {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

/* Override Blueprint's _reset.scss styles */
html {
  box-sizing: unset;
}

*,
*::before,
*::after {
  box-sizing: unset;
}

body {
  color: unset;
  font-family: var(--jp-ui-font-family);
}

p {
  margin-top: unset;
  margin-bottom: unset;
}

small {
  font-size: unset;
}

strong {
  font-weight: unset;
}

/* Override Blueprint's _typography.scss styles */
a {
  text-decoration: unset;
  color: unset;
}
a:hover {
  text-decoration: unset;
  color: unset;
}

/* Override Blueprint's _accessibility.scss styles */
:focus {
  outline: unset;
  outline-offset: unset;
  -moz-outline-radius: unset;
}

/* Styles for ui-components */
.jp-Button {
  border-radius: var(--jp-border-radius);
  padding: 0px 12px;
  font-size: var(--jp-ui-font-size1);
}

/* Use our own theme for hover styles */
button.jp-Button.bp3-button.bp3-minimal:hover {
  background-color: var(--jp-layout-color2);
}
.jp-Button.minimal {
  color: unset !important;
}

.jp-Button.jp-ToolbarButtonComponent {
  text-transform: none;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color3);
}

.jp-BPIcon {
  display: inline-block;
  vertical-align: middle;
  margin: auto;
}

/* Stop blueprint futzing with our icon fills */
.bp3-icon.jp-BPIcon > svg:not([fill]) {
  fill: var(--jp-inverse-layout-color3);
}

.jp-InputGroupAction {
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

/* Use our own theme for hover and option styles */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}
select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-top: 1px solid var(--jp-border-color2);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-Collapse-header {
  padding: 1px 12px;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size2);
}

.jp-Collapse-header:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Collapse-contents {
  padding: 0px 12px 0px 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0px;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0px 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.lm-CommandPalette-wrapper::after {
  content: ' ';
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  height: 30px;
  width: 10px;
  padding: 0px 10px;
  background-image: var(--jp-icon-search-white);
  background-size: 20px;
  background-repeat: no-repeat;
  background-position: center;
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color3);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0px;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color3);
}

.lm-CommandPalette-item.lm-mod-active {
  background: var(--jp-layout-color3);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  background: var(--jp-layout-color4);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color3);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.4;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty:after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0px 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0px;
  left: 0px;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px;
  padding-bottom: 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0px;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

.jp-Dialog-header {
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0px 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

.jp-HoverBox.jp-mod-outofview {
  display: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;

  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;

  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #aa00ff;

  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;

  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;

  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;

  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;

  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;

  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;

  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;

  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;

  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;

  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ffff00;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;

  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;

  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;

  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;

  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;

  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eeeeee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent:before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent:after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0px 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  height: 28px;
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  background-color: var(--jp-layout-color1);
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0px 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  height: 32px;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 1;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px;
  margin: 0px;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px 6px;
  margin: 0px;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent span {
  padding: 0px;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ body.p-mod-override-cursor *, /* </DEPRECATED> */
body.lm-mod-override-cursor * {
  cursor: inherit !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 300px;
  color: black;
  direction: ltr;
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
}
.CodeMirror-linenumbers {}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker { color: black; }
.CodeMirror-guttermarker-subtle { color: #999; }

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0 !important;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}
.cm-fat-cursor-mark {
  background-color: rgba(20, 255, 20, 0.5);
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
}
.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@-webkit-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {}

.cm-tab { display: inline-block; text-decoration: inherit; }

.CodeMirror-rulers {
  position: absolute;
  left: 0; right: 0; top: -50px; bottom: 0;
  overflow: hidden;
}
.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  top: 0; bottom: 0;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {color: blue;}
.cm-s-default .cm-quote {color: #090;}
.cm-negative {color: #d44;}
.cm-positive {color: #292;}
.cm-header, .cm-strong {font-weight: bold;}
.cm-em {font-style: italic;}
.cm-link {text-decoration: underline;}
.cm-strikethrough {text-decoration: line-through;}

.cm-s-default .cm-keyword {color: #708;}
.cm-s-default .cm-atom {color: #219;}
.cm-s-default .cm-number {color: #164;}
.cm-s-default .cm-def {color: #00f;}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {}
.cm-s-default .cm-variable-2 {color: #05a;}
.cm-s-default .cm-variable-3, .cm-s-default .cm-type {color: #085;}
.cm-s-default .cm-comment {color: #a50;}
.cm-s-default .cm-string {color: #a11;}
.cm-s-default .cm-string-2 {color: #f50;}
.cm-s-default .cm-meta {color: #555;}
.cm-s-default .cm-qualifier {color: #555;}
.cm-s-default .cm-builtin {color: #30a;}
.cm-s-default .cm-bracket {color: #997;}
.cm-s-default .cm-tag {color: #170;}
.cm-s-default .cm-attribute {color: #00c;}
.cm-s-default .cm-hr {color: #999;}
.cm-s-default .cm-link {color: #00c;}

.cm-s-default .cm-error {color: #f00;}
.cm-invalidchar {color: #f00;}

.CodeMirror-composing { border-bottom: 2px solid; }

/* Default styles for common addons */

div.CodeMirror span.CodeMirror-matchingbracket {color: #0b0;}
div.CodeMirror span.CodeMirror-nonmatchingbracket {color: #a22;}
.CodeMirror-matchingtag { background: rgba(255, 150, 0, .3); }
.CodeMirror-activeline-background {background: #e8f2ff;}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white;
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 30px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -30px; margin-right: -30px;
  padding-bottom: 30px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative;
}
.CodeMirror-sizer {
  position: relative;
  border-right: 30px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
}
.CodeMirror-vscrollbar {
  right: 0; top: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.CodeMirror-hscrollbar {
  bottom: 0; left: 0;
  overflow-y: hidden;
  overflow-x: scroll;
}
.CodeMirror-scrollbar-filler {
  right: 0; bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0; bottom: 0;
}

.CodeMirror-gutters {
  position: absolute; left: 0; top: 0;
  min-height: 100%;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  vertical-align: top;
  margin-bottom: -30px;
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0; bottom: 0;
  z-index: 4;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper ::selection { background-color: transparent }
.CodeMirror-gutter-wrapper ::-moz-selection { background-color: transparent }

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0; -webkit-border-radius: 0; border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-variant-ligatures: contextual;
  font-variant-ligatures: contextual;
}
.CodeMirror-wrap pre.CodeMirror-line,
.CodeMirror-wrap pre.CodeMirror-line-like {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0; right: 0; top: 0; bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  padding: 0.1px; /* Force widget margins to stay inside of the container */
}

.CodeMirror-widget {}

.CodeMirror-rtl pre { direction: rtl; }

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
  pointer-events: none;
}
.CodeMirror-measure pre { position: static; }

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
}

.CodeMirror-selected { background: #d9d9d9; }
.CodeMirror-focused .CodeMirror-selected { background: #d7d4f0; }
.CodeMirror-crosshair { cursor: crosshair; }
.CodeMirror-line::selection, .CodeMirror-line > span::selection, .CodeMirror-line > span > span::selection { background: #d7d4f0; }
.CodeMirror-line::-moz-selection, .CodeMirror-line > span::-moz-selection, .CodeMirror-line > span > span::-moz-selection { background: #d7d4f0; }

.cm-searching {
  background-color: #ffa;
  background-color: rgba(255, 255, 0, .4);
}

/* Used to force a border model for a node */
.cm-force-border { padding-right: .1px; }

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after { content: ''; }

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext { background: none; }

.CodeMirror-dialog {
  position: absolute;
  left: 0; right: 0;
  background: inherit;
  z-index: 15;
  padding: .1em .8em;
  overflow: hidden;
  color: inherit;
}

.CodeMirror-dialog-top {
  border-bottom: 1px solid #eee;
  top: 0;
}

.CodeMirror-dialog-bottom {
  border-top: 1px solid #eee;
  bottom: 0;
}

.CodeMirror-dialog input {
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
}

.CodeMirror-dialog button {
  font-size: 70%;
}

.CodeMirror-foldmarker {
  color: blue;
  text-shadow: #b9f 1px 1px 2px, #b9f -1px -1px 2px, #b9f 1px -1px 2px, #b9f -1px 1px 2px;
  font-family: arial;
  line-height: .3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: .7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}

/*
  Name:       material
  Author:     Mattia Astorino (http://github.com/equinusocio)
  Website:    https://material-theme.site/
*/

.cm-s-material.CodeMirror {
  background-color: #263238;
  color: #EEFFFF;
}

.cm-s-material .CodeMirror-gutters {
  background: #263238;
  color: #546E7A;
  border: none;
}

.cm-s-material .CodeMirror-guttermarker,
.cm-s-material .CodeMirror-guttermarker-subtle,
.cm-s-material .CodeMirror-linenumber {
  color: #546E7A;
}

.cm-s-material .CodeMirror-cursor {
  border-left: 1px solid #FFCC00;
}

.cm-s-material div.CodeMirror-selected {
  background: rgba(128, 203, 196, 0.2);
}

.cm-s-material.CodeMirror-focused div.CodeMirror-selected {
  background: rgba(128, 203, 196, 0.2);
}

.cm-s-material .CodeMirror-line::selection,
.cm-s-material .CodeMirror-line>span::selection,
.cm-s-material .CodeMirror-line>span>span::selection {
  background: rgba(128, 203, 196, 0.2);
}

.cm-s-material .CodeMirror-line::-moz-selection,
.cm-s-material .CodeMirror-line>span::-moz-selection,
.cm-s-material .CodeMirror-line>span>span::-moz-selection {
  background: rgba(128, 203, 196, 0.2);
}

.cm-s-material .CodeMirror-activeline-background {
  background: rgba(0, 0, 0, 0.5);
}

.cm-s-material .cm-keyword {
  color: #C792EA;
}

.cm-s-material .cm-operator {
  color: #89DDFF;
}

.cm-s-material .cm-variable-2 {
  color: #EEFFFF;
}

.cm-s-material .cm-variable-3,
.cm-s-material .cm-type {
  color: #f07178;
}

.cm-s-material .cm-builtin {
  color: #FFCB6B;
}

.cm-s-material .cm-atom {
  color: #F78C6C;
}

.cm-s-material .cm-number {
  color: #FF5370;
}

.cm-s-material .cm-def {
  color: #82AAFF;
}

.cm-s-material .cm-string {
  color: #C3E88D;
}

.cm-s-material .cm-string-2 {
  color: #f07178;
}

.cm-s-material .cm-comment {
  color: #546E7A;
}

.cm-s-material .cm-variable {
  color: #f07178;
}

.cm-s-material .cm-tag {
  color: #FF5370;
}

.cm-s-material .cm-meta {
  color: #FFCB6B;
}

.cm-s-material .cm-attribute {
  color: #C792EA;
}

.cm-s-material .cm-property {
  color: #C792EA;
}

.cm-s-material .cm-qualifier {
  color: #DECB6B;
}

.cm-s-material .cm-variable-3,
.cm-s-material .cm-type {
  color: #DECB6B;
}


.cm-s-material .cm-error {
  color: rgba(255, 255, 255, 1.0);
  background-color: #FF5370;
}

.cm-s-material .CodeMirror-matchingbracket {
  text-decoration: underline;
  color: white !important;
}
/**
 * "
 *  Using Zenburn color palette from the Emacs Zenburn Theme
 *  https://github.com/bbatsov/zenburn-emacs/blob/master/zenburn-theme.el
 *
 *  Also using parts of https://github.com/xavi/coderay-lighttable-theme
 * "
 * From: https://github.com/wisenomad/zenburn-lighttable-theme/blob/master/zenburn.css
 */

.cm-s-zenburn .CodeMirror-gutters { background: #3f3f3f !important; }
.cm-s-zenburn .CodeMirror-foldgutter-open, .CodeMirror-foldgutter-folded { color: #999; }
.cm-s-zenburn .CodeMirror-cursor { border-left: 1px solid white; }
.cm-s-zenburn { background-color: #3f3f3f; color: #dcdccc; }
.cm-s-zenburn span.cm-builtin { color: #dcdccc; font-weight: bold; }
.cm-s-zenburn span.cm-comment { color: #7f9f7f; }
.cm-s-zenburn span.cm-keyword { color: #f0dfaf; font-weight: bold; }
.cm-s-zenburn span.cm-atom { color: #bfebbf; }
.cm-s-zenburn span.cm-def { color: #dcdccc; }
.cm-s-zenburn span.cm-variable { color: #dfaf8f; }
.cm-s-zenburn span.cm-variable-2 { color: #dcdccc; }
.cm-s-zenburn span.cm-string { color: #cc9393; }
.cm-s-zenburn span.cm-string-2 { color: #cc9393; }
.cm-s-zenburn span.cm-number { color: #dcdccc; }
.cm-s-zenburn span.cm-tag { color: #93e0e3; }
.cm-s-zenburn span.cm-property { color: #dfaf8f; }
.cm-s-zenburn span.cm-attribute { color: #dfaf8f; }
.cm-s-zenburn span.cm-qualifier { color: #7cb8bb; }
.cm-s-zenburn span.cm-meta { color: #f0dfaf; }
.cm-s-zenburn span.cm-header { color: #f0efd0; }
.cm-s-zenburn span.cm-operator { color: #f0efd0; }
.cm-s-zenburn span.CodeMirror-matchingbracket { box-sizing: border-box; background: transparent; border-bottom: 1px solid; }
.cm-s-zenburn span.CodeMirror-nonmatchingbracket { border-bottom: 1px solid; background: none; }
.cm-s-zenburn .CodeMirror-activeline { background: #000000; }
.cm-s-zenburn .CodeMirror-activeline-background { background: #000000; }
.cm-s-zenburn div.CodeMirror-selected { background: #545454; }
.cm-s-zenburn .CodeMirror-focused div.CodeMirror-selected { background: #4f4f4f; }

.cm-s-abcdef.CodeMirror { background: #0f0f0f; color: #defdef; }
.cm-s-abcdef div.CodeMirror-selected { background: #515151; }
.cm-s-abcdef .CodeMirror-line::selection, .cm-s-abcdef .CodeMirror-line > span::selection, .cm-s-abcdef .CodeMirror-line > span > span::selection { background: rgba(56, 56, 56, 0.99); }
.cm-s-abcdef .CodeMirror-line::-moz-selection, .cm-s-abcdef .CodeMirror-line > span::-moz-selection, .cm-s-abcdef .CodeMirror-line > span > span::-moz-selection { background: rgba(56, 56, 56, 0.99); }
.cm-s-abcdef .CodeMirror-gutters { background: #555; border-right: 2px solid #314151; }
.cm-s-abcdef .CodeMirror-guttermarker { color: #222; }
.cm-s-abcdef .CodeMirror-guttermarker-subtle { color: azure; }
.cm-s-abcdef .CodeMirror-linenumber { color: #FFFFFF; }
.cm-s-abcdef .CodeMirror-cursor { border-left: 1px solid #00FF00; }

.cm-s-abcdef span.cm-keyword { color: darkgoldenrod; font-weight: bold; }
.cm-s-abcdef span.cm-atom { color: #77F; }
.cm-s-abcdef span.cm-number { color: violet; }
.cm-s-abcdef span.cm-def { color: #fffabc; }
.cm-s-abcdef span.cm-variable { color: #abcdef; }
.cm-s-abcdef span.cm-variable-2 { color: #cacbcc; }
.cm-s-abcdef span.cm-variable-3, .cm-s-abcdef span.cm-type { color: #def; }
.cm-s-abcdef span.cm-property { color: #fedcba; }
.cm-s-abcdef span.cm-operator { color: #ff0; }
.cm-s-abcdef span.cm-comment { color: #7a7b7c; font-style: italic;}
.cm-s-abcdef span.cm-string { color: #2b4; }
.cm-s-abcdef span.cm-meta { color: #C9F; }
.cm-s-abcdef span.cm-qualifier { color: #FFF700; }
.cm-s-abcdef span.cm-builtin { color: #30aabc; }
.cm-s-abcdef span.cm-bracket { color: #8a8a8a; }
.cm-s-abcdef span.cm-tag { color: #FFDD44; }
.cm-s-abcdef span.cm-attribute { color: #DDFF00; }
.cm-s-abcdef span.cm-error { color: #FF0000; }
.cm-s-abcdef span.cm-header { color: aquamarine; font-weight: bold; }
.cm-s-abcdef span.cm-link { color: blueviolet; }

.cm-s-abcdef .CodeMirror-activeline-background { background: #314151; }

/*

    Name:       Base16 Default Light
    Author:     Chris Kempson (http://chriskempson.com)

    CodeMirror template by Jan T. Sott (https://github.com/idleberg/base16-codemirror)
    Original Base16 color scheme by Chris Kempson (https://github.com/chriskempson/base16)

*/

.cm-s-base16-light.CodeMirror { background: #f5f5f5; color: #202020; }
.cm-s-base16-light div.CodeMirror-selected { background: #e0e0e0; }
.cm-s-base16-light .CodeMirror-line::selection, .cm-s-base16-light .CodeMirror-line > span::selection, .cm-s-base16-light .CodeMirror-line > span > span::selection { background: #e0e0e0; }
.cm-s-base16-light .CodeMirror-line::-moz-selection, .cm-s-base16-light .CodeMirror-line > span::-moz-selection, .cm-s-base16-light .CodeMirror-line > span > span::-moz-selection { background: #e0e0e0; }
.cm-s-base16-light .CodeMirror-gutters { background: #f5f5f5; border-right: 0px; }
.cm-s-base16-light .CodeMirror-guttermarker { color: #ac4142; }
.cm-s-base16-light .CodeMirror-guttermarker-subtle { color: #b0b0b0; }
.cm-s-base16-light .CodeMirror-linenumber { color: #b0b0b0; }
.cm-s-base16-light .CodeMirror-cursor { border-left: 1px solid #505050; }

.cm-s-base16-light span.cm-comment { color: #8f5536; }
.cm-s-base16-light span.cm-atom { color: #aa759f; }
.cm-s-base16-light span.cm-number { color: #aa759f; }

.cm-s-base16-light span.cm-property, .cm-s-base16-light span.cm-attribute { color: #90a959; }
.cm-s-base16-light span.cm-keyword { color: #ac4142; }
.cm-s-base16-light span.cm-string { color: #f4bf75; }

.cm-s-base16-light span.cm-variable { color: #90a959; }
.cm-s-base16-light span.cm-variable-2 { color: #6a9fb5; }
.cm-s-base16-light span.cm-def { color: #d28445; }
.cm-s-base16-light span.cm-bracket { color: #202020; }
.cm-s-base16-light span.cm-tag { color: #ac4142; }
.cm-s-base16-light span.cm-link { color: #aa759f; }
.cm-s-base16-light span.cm-error { background: #ac4142; color: #505050; }

.cm-s-base16-light .CodeMirror-activeline-background { background: #DDDCDC; }
.cm-s-base16-light .CodeMirror-matchingbracket { color: #f5f5f5 !important; background-color: #6A9FB5 !important}

/*

    Name:       Base16 Default Dark
    Author:     Chris Kempson (http://chriskempson.com)

    CodeMirror template by Jan T. Sott (https://github.com/idleberg/base16-codemirror)
    Original Base16 color scheme by Chris Kempson (https://github.com/chriskempson/base16)

*/

.cm-s-base16-dark.CodeMirror { background: #151515; color: #e0e0e0; }
.cm-s-base16-dark div.CodeMirror-selected { background: #303030; }
.cm-s-base16-dark .CodeMirror-line::selection, .cm-s-base16-dark .CodeMirror-line > span::selection, .cm-s-base16-dark .CodeMirror-line > span > span::selection { background: rgba(48, 48, 48, .99); }
.cm-s-base16-dark .CodeMirror-line::-moz-selection, .cm-s-base16-dark .CodeMirror-line > span::-moz-selection, .cm-s-base16-dark .CodeMirror-line > span > span::-moz-selection { background: rgba(48, 48, 48, .99); }
.cm-s-base16-dark .CodeMirror-gutters { background: #151515; border-right: 0px; }
.cm-s-base16-dark .CodeMirror-guttermarker { color: #ac4142; }
.cm-s-base16-dark .CodeMirror-guttermarker-subtle { color: #505050; }
.cm-s-base16-dark .CodeMirror-linenumber { color: #505050; }
.cm-s-base16-dark .CodeMirror-cursor { border-left: 1px solid #b0b0b0; }

.cm-s-base16-dark span.cm-comment { color: #8f5536; }
.cm-s-base16-dark span.cm-atom { color: #aa759f; }
.cm-s-base16-dark span.cm-number { color: #aa759f; }

.cm-s-base16-dark span.cm-property, .cm-s-base16-dark span.cm-attribute { color: #90a959; }
.cm-s-base16-dark span.cm-keyword { color: #ac4142; }
.cm-s-base16-dark span.cm-string { color: #f4bf75; }

.cm-s-base16-dark span.cm-variable { color: #90a959; }
.cm-s-base16-dark span.cm-variable-2 { color: #6a9fb5; }
.cm-s-base16-dark span.cm-def { color: #d28445; }
.cm-s-base16-dark span.cm-bracket { color: #e0e0e0; }
.cm-s-base16-dark span.cm-tag { color: #ac4142; }
.cm-s-base16-dark span.cm-link { color: #aa759f; }
.cm-s-base16-dark span.cm-error { background: #ac4142; color: #b0b0b0; }

.cm-s-base16-dark .CodeMirror-activeline-background { background: #202020; }
.cm-s-base16-dark .CodeMirror-matchingbracket { text-decoration: underline; color: white !important; }

/*

    Name:       dracula
    Author:     Michael Kaminsky (http://github.com/mkaminsky11)

    Original dracula color scheme by Zeno Rocha (https://github.com/zenorocha/dracula-theme)

*/


.cm-s-dracula.CodeMirror, .cm-s-dracula .CodeMirror-gutters {
  background-color: #282a36 !important;
  color: #f8f8f2 !important;
  border: none;
}
.cm-s-dracula .CodeMirror-gutters { color: #282a36; }
.cm-s-dracula .CodeMirror-cursor { border-left: solid thin #f8f8f0; }
.cm-s-dracula .CodeMirror-linenumber { color: #6D8A88; }
.cm-s-dracula .CodeMirror-selected { background: rgba(255, 255, 255, 0.10); }
.cm-s-dracula .CodeMirror-line::selection, .cm-s-dracula .CodeMirror-line > span::selection, .cm-s-dracula .CodeMirror-line > span > span::selection { background: rgba(255, 255, 255, 0.10); }
.cm-s-dracula .CodeMirror-line::-moz-selection, .cm-s-dracula .CodeMirror-line > span::-moz-selection, .cm-s-dracula .CodeMirror-line > span > span::-moz-selection { background: rgba(255, 255, 255, 0.10); }
.cm-s-dracula span.cm-comment { color: #6272a4; }
.cm-s-dracula span.cm-string, .cm-s-dracula span.cm-string-2 { color: #f1fa8c; }
.cm-s-dracula span.cm-number { color: #bd93f9; }
.cm-s-dracula span.cm-variable { color: #50fa7b; }
.cm-s-dracula span.cm-variable-2 { color: white; }
.cm-s-dracula span.cm-def { color: #50fa7b; }
.cm-s-dracula span.cm-operator { color: #ff79c6; }
.cm-s-dracula span.cm-keyword { color: #ff79c6; }
.cm-s-dracula span.cm-atom { color: #bd93f9; }
.cm-s-dracula span.cm-meta { color: #f8f8f2; }
.cm-s-dracula span.cm-tag { color: #ff79c6; }
.cm-s-dracula span.cm-attribute { color: #50fa7b; }
.cm-s-dracula span.cm-qualifier { color: #50fa7b; }
.cm-s-dracula span.cm-property { color: #66d9ef; }
.cm-s-dracula span.cm-builtin { color: #50fa7b; }
.cm-s-dracula span.cm-variable-3, .cm-s-dracula span.cm-type { color: #ffb86c; }

.cm-s-dracula .CodeMirror-activeline-background { background: rgba(255,255,255,0.1); }
.cm-s-dracula .CodeMirror-matchingbracket { text-decoration: underline; color: white !important; }

/*

    Name:       Hopscotch
    Author:     Jan T. Sott

    CodeMirror template by Jan T. Sott (https://github.com/idleberg/base16-codemirror)
    Original Base16 color scheme by Chris Kempson (https://github.com/chriskempson/base16)

*/

.cm-s-hopscotch.CodeMirror {background: #322931; color: #d5d3d5;}
.cm-s-hopscotch div.CodeMirror-selected {background: #433b42 !important;}
.cm-s-hopscotch .CodeMirror-gutters {background: #322931; border-right: 0px;}
.cm-s-hopscotch .CodeMirror-linenumber {color: #797379;}
.cm-s-hopscotch .CodeMirror-cursor {border-left: 1px solid #989498 !important;}

.cm-s-hopscotch span.cm-comment {color: #b33508;}
.cm-s-hopscotch span.cm-atom {color: #c85e7c;}
.cm-s-hopscotch span.cm-number {color: #c85e7c;}

.cm-s-hopscotch span.cm-property, .cm-s-hopscotch span.cm-attribute {color: #8fc13e;}
.cm-s-hopscotch span.cm-keyword {color: #dd464c;}
.cm-s-hopscotch span.cm-string {color: #fdcc59;}

.cm-s-hopscotch span.cm-variable {color: #8fc13e;}
.cm-s-hopscotch span.cm-variable-2 {color: #1290bf;}
.cm-s-hopscotch span.cm-def {color: #fd8b19;}
.cm-s-hopscotch span.cm-error {background: #dd464c; color: #989498;}
.cm-s-hopscotch span.cm-bracket {color: #d5d3d5;}
.cm-s-hopscotch span.cm-tag {color: #dd464c;}
.cm-s-hopscotch span.cm-link {color: #c85e7c;}

.cm-s-hopscotch .CodeMirror-matchingbracket { text-decoration: underline; color: white !important;}
.cm-s-hopscotch .CodeMirror-activeline-background { background: #302020; }

/****************************************************************/
/*   Based on mbonaci's Brackets mbo theme                      */
/*   https://github.com/mbonaci/global/blob/master/Mbo.tmTheme  */
/*   Create your own: http://tmtheme-editor.herokuapp.com       */
/****************************************************************/

.cm-s-mbo.CodeMirror { background: #2c2c2c; color: #ffffec; }
.cm-s-mbo div.CodeMirror-selected { background: #716C62; }
.cm-s-mbo .CodeMirror-line::selection, .cm-s-mbo .CodeMirror-line > span::selection, .cm-s-mbo .CodeMirror-line > span > span::selection { background: rgba(113, 108, 98, .99); }
.cm-s-mbo .CodeMirror-line::-moz-selection, .cm-s-mbo .CodeMirror-line > span::-moz-selection, .cm-s-mbo .CodeMirror-line > span > span::-moz-selection { background: rgba(113, 108, 98, .99); }
.cm-s-mbo .CodeMirror-gutters { background: #4e4e4e; border-right: 0px; }
.cm-s-mbo .CodeMirror-guttermarker { color: white; }
.cm-s-mbo .CodeMirror-guttermarker-subtle { color: grey; }
.cm-s-mbo .CodeMirror-linenumber { color: #dadada; }
.cm-s-mbo .CodeMirror-cursor { border-left: 1px solid #ffffec; }

.cm-s-mbo span.cm-comment { color: #95958a; }
.cm-s-mbo span.cm-atom { color: #00a8c6; }
.cm-s-mbo span.cm-number { color: #00a8c6; }

.cm-s-mbo span.cm-property, .cm-s-mbo span.cm-attribute { color: #9ddfe9; }
.cm-s-mbo span.cm-keyword { color: #ffb928; }
.cm-s-mbo span.cm-string { color: #ffcf6c; }
.cm-s-mbo span.cm-string.cm-property { color: #ffffec; }

.cm-s-mbo span.cm-variable { color: #ffffec; }
.cm-s-mbo span.cm-variable-2 { color: #00a8c6; }
.cm-s-mbo span.cm-def { color: #ffffec; }
.cm-s-mbo span.cm-bracket { color: #fffffc; font-weight: bold; }
.cm-s-mbo span.cm-tag { color: #9ddfe9; }
.cm-s-mbo span.cm-link { color: #f54b07; }
.cm-s-mbo span.cm-error { border-bottom: #636363; color: #ffffec; }
.cm-s-mbo span.cm-qualifier { color: #ffffec; }

.cm-s-mbo .CodeMirror-activeline-background { background: #494b41; }
.cm-s-mbo .CodeMirror-matchingbracket { color: #ffb928 !important; }
.cm-s-mbo .CodeMirror-matchingtag { background: rgba(255, 255, 255, .37); }

/*
  MDN-LIKE Theme - Mozilla
  Ported to CodeMirror by Peter Kroon <plakroon@gmail.com>
  Report bugs/issues here: https://github.com/codemirror/CodeMirror/issues
  GitHub: @peterkroon

  The mdn-like theme is inspired on the displayed code examples at: https://developer.mozilla.org/en-US/docs/Web/CSS/animation

*/
.cm-s-mdn-like.CodeMirror { color: #999; background-color: #fff; }
.cm-s-mdn-like div.CodeMirror-selected { background: #cfc; }
.cm-s-mdn-like .CodeMirror-line::selection, .cm-s-mdn-like .CodeMirror-line > span::selection, .cm-s-mdn-like .CodeMirror-line > span > span::selection { background: #cfc; }
.cm-s-mdn-like .CodeMirror-line::-moz-selection, .cm-s-mdn-like .CodeMirror-line > span::-moz-selection, .cm-s-mdn-like .CodeMirror-line > span > span::-moz-selection { background: #cfc; }

.cm-s-mdn-like .CodeMirror-gutters { background: #f8f8f8; border-left: 6px solid rgba(0,83,159,0.65); color: #333; }
.cm-s-mdn-like .CodeMirror-linenumber { color: #aaa; padding-left: 8px; }
.cm-s-mdn-like .CodeMirror-cursor { border-left: 2px solid #222; }

.cm-s-mdn-like .cm-keyword { color: #6262FF; }
.cm-s-mdn-like .cm-atom { color: #F90; }
.cm-s-mdn-like .cm-number { color:  #ca7841; }
.cm-s-mdn-like .cm-def { color: #8DA6CE; }
.cm-s-mdn-like span.cm-variable-2, .cm-s-mdn-like span.cm-tag { color: #690; }
.cm-s-mdn-like span.cm-variable-3, .cm-s-mdn-like span.cm-def, .cm-s-mdn-like span.cm-type { color: #07a; }

.cm-s-mdn-like .cm-variable { color: #07a; }
.cm-s-mdn-like .cm-property { color: #905; }
.cm-s-mdn-like .cm-qualifier { color: #690; }

.cm-s-mdn-like .cm-operator { color: #cda869; }
.cm-s-mdn-like .cm-comment { color:#777; font-weight:normal; }
.cm-s-mdn-like .cm-string { color:#07a; font-style:italic; }
.cm-s-mdn-like .cm-string-2 { color:#bd6b18; } /*?*/
.cm-s-mdn-like .cm-meta { color: #000; } /*?*/
.cm-s-mdn-like .cm-builtin { color: #9B7536; } /*?*/
.cm-s-mdn-like .cm-tag { color: #997643; }
.cm-s-mdn-like .cm-attribute { color: #d6bb6d; } /*?*/
.cm-s-mdn-like .cm-header { color: #FF6400; }
.cm-s-mdn-like .cm-hr { color: #AEAEAE; }
.cm-s-mdn-like .cm-link { color:#ad9361; font-style:italic; text-decoration:none; }
.cm-s-mdn-like .cm-error { border-bottom: 1px solid red; }

div.cm-s-mdn-like .CodeMirror-activeline-background { background: #efefff; }
div.cm-s-mdn-like span.CodeMirror-matchingbracket { outline:1px solid grey; color: inherit; }

.cm-s-mdn-like.CodeMirror { background-image: url(data:image/png;base64,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); }

/*

    Name:       seti
    Author:     Michael Kaminsky (http://github.com/mkaminsky11)

    Original seti color scheme by Jesse Weed (https://github.com/jesseweed/seti-syntax)

*/


.cm-s-seti.CodeMirror {
  background-color: #151718 !important;
  color: #CFD2D1 !important;
  border: none;
}
.cm-s-seti .CodeMirror-gutters {
  color: #404b53;
  background-color: #0E1112;
  border: none;
}
.cm-s-seti .CodeMirror-cursor { border-left: solid thin #f8f8f0; }
.cm-s-seti .CodeMirror-linenumber { color: #6D8A88; }
.cm-s-seti.CodeMirror-focused div.CodeMirror-selected { background: rgba(255, 255, 255, 0.10); }
.cm-s-seti .CodeMirror-line::selection, .cm-s-seti .CodeMirror-line > span::selection, .cm-s-seti .CodeMirror-line > span > span::selection { background: rgba(255, 255, 255, 0.10); }
.cm-s-seti .CodeMirror-line::-moz-selection, .cm-s-seti .CodeMirror-line > span::-moz-selection, .cm-s-seti .CodeMirror-line > span > span::-moz-selection { background: rgba(255, 255, 255, 0.10); }
.cm-s-seti span.cm-comment { color: #41535b; }
.cm-s-seti span.cm-string, .cm-s-seti span.cm-string-2 { color: #55b5db; }
.cm-s-seti span.cm-number { color: #cd3f45; }
.cm-s-seti span.cm-variable { color: #55b5db; }
.cm-s-seti span.cm-variable-2 { color: #a074c4; }
.cm-s-seti span.cm-def { color: #55b5db; }
.cm-s-seti span.cm-keyword { color: #ff79c6; }
.cm-s-seti span.cm-operator { color: #9fca56; }
.cm-s-seti span.cm-keyword { color: #e6cd69; }
.cm-s-seti span.cm-atom { color: #cd3f45; }
.cm-s-seti span.cm-meta { color: #55b5db; }
.cm-s-seti span.cm-tag { color: #55b5db; }
.cm-s-seti span.cm-attribute { color: #9fca56; }
.cm-s-seti span.cm-qualifier { color: #9fca56; }
.cm-s-seti span.cm-property { color: #a074c4; }
.cm-s-seti span.cm-variable-3, .cm-s-seti span.cm-type { color: #9fca56; }
.cm-s-seti span.cm-builtin { color: #9fca56; }
.cm-s-seti .CodeMirror-activeline-background { background: #101213; }
.cm-s-seti .CodeMirror-matchingbracket { text-decoration: underline; color: white !important; }

/*
Solarized theme for code-mirror
http://ethanschoonover.com/solarized
*/

/*
Solarized color palette
http://ethanschoonover.com/solarized/img/solarized-palette.png
*/

.solarized.base03 { color: #002b36; }
.solarized.base02 { color: #073642; }
.solarized.base01 { color: #586e75; }
.solarized.base00 { color: #657b83; }
.solarized.base0 { color: #839496; }
.solarized.base1 { color: #93a1a1; }
.solarized.base2 { color: #eee8d5; }
.solarized.base3  { color: #fdf6e3; }
.solarized.solar-yellow  { color: #b58900; }
.solarized.solar-orange  { color: #cb4b16; }
.solarized.solar-red { color: #dc322f; }
.solarized.solar-magenta { color: #d33682; }
.solarized.solar-violet  { color: #6c71c4; }
.solarized.solar-blue { color: #268bd2; }
.solarized.solar-cyan { color: #2aa198; }
.solarized.solar-green { color: #859900; }

/* Color scheme for code-mirror */

.cm-s-solarized {
  line-height: 1.45em;
  color-profile: sRGB;
  rendering-intent: auto;
}
.cm-s-solarized.cm-s-dark {
  color: #839496;
  background-color: #002b36;
  text-shadow: #002b36 0 1px;
}
.cm-s-solarized.cm-s-light {
  background-color: #fdf6e3;
  color: #657b83;
  text-shadow: #eee8d5 0 1px;
}

.cm-s-solarized .CodeMirror-widget {
  text-shadow: none;
}

.cm-s-solarized .cm-header { color: #586e75; }
.cm-s-solarized .cm-quote { color: #93a1a1; }

.cm-s-solarized .cm-keyword { color: #cb4b16; }
.cm-s-solarized .cm-atom { color: #d33682; }
.cm-s-solarized .cm-number { color: #d33682; }
.cm-s-solarized .cm-def { color: #2aa198; }

.cm-s-solarized .cm-variable { color: #839496; }
.cm-s-solarized .cm-variable-2 { color: #b58900; }
.cm-s-solarized .cm-variable-3, .cm-s-solarized .cm-type { color: #6c71c4; }

.cm-s-solarized .cm-property { color: #2aa198; }
.cm-s-solarized .cm-operator { color: #6c71c4; }

.cm-s-solarized .cm-comment { color: #586e75; font-style:italic; }

.cm-s-solarized .cm-string { color: #859900; }
.cm-s-solarized .cm-string-2 { color: #b58900; }

.cm-s-solarized .cm-meta { color: #859900; }
.cm-s-solarized .cm-qualifier { color: #b58900; }
.cm-s-solarized .cm-builtin { color: #d33682; }
.cm-s-solarized .cm-bracket { color: #cb4b16; }
.cm-s-solarized .CodeMirror-matchingbracket { color: #859900; }
.cm-s-solarized .CodeMirror-nonmatchingbracket { color: #dc322f; }
.cm-s-solarized .cm-tag { color: #93a1a1; }
.cm-s-solarized .cm-attribute { color: #2aa198; }
.cm-s-solarized .cm-hr {
  color: transparent;
  border-top: 1px solid #586e75;
  display: block;
}
.cm-s-solarized .cm-link { color: #93a1a1; cursor: pointer; }
.cm-s-solarized .cm-special { color: #6c71c4; }
.cm-s-solarized .cm-em {
  color: #999;
  text-decoration: underline;
  text-decoration-style: dotted;
}
.cm-s-solarized .cm-error,
.cm-s-solarized .cm-invalidchar {
  color: #586e75;
  border-bottom: 1px dotted #dc322f;
}

.cm-s-solarized.cm-s-dark div.CodeMirror-selected { background: #073642; }
.cm-s-solarized.cm-s-dark.CodeMirror ::selection { background: rgba(7, 54, 66, 0.99); }
.cm-s-solarized.cm-s-dark .CodeMirror-line::-moz-selection, .cm-s-dark .CodeMirror-line > span::-moz-selection, .cm-s-dark .CodeMirror-line > span > span::-moz-selection { background: rgba(7, 54, 66, 0.99); }

.cm-s-solarized.cm-s-light div.CodeMirror-selected { background: #eee8d5; }
.cm-s-solarized.cm-s-light .CodeMirror-line::selection, .cm-s-light .CodeMirror-line > span::selection, .cm-s-light .CodeMirror-line > span > span::selection { background: #eee8d5; }
.cm-s-solarized.cm-s-light .CodeMirror-line::-moz-selection, .cm-s-ligh .CodeMirror-line > span::-moz-selection, .cm-s-ligh .CodeMirror-line > span > span::-moz-selection { background: #eee8d5; }

/* Editor styling */



/* Little shadow on the view-port of the buffer view */
.cm-s-solarized.CodeMirror {
  -moz-box-shadow: inset 7px 0 12px -6px #000;
  -webkit-box-shadow: inset 7px 0 12px -6px #000;
  box-shadow: inset 7px 0 12px -6px #000;
}

/* Remove gutter border */
.cm-s-solarized .CodeMirror-gutters {
  border-right: 0;
}

/* Gutter colors and line number styling based of color scheme (dark / light) */

/* Dark */
.cm-s-solarized.cm-s-dark .CodeMirror-gutters {
  background-color: #073642;
}

.cm-s-solarized.cm-s-dark .CodeMirror-linenumber {
  color: #586e75;
  text-shadow: #021014 0 -1px;
}

/* Light */
.cm-s-solarized.cm-s-light .CodeMirror-gutters {
  background-color: #eee8d5;
}

.cm-s-solarized.cm-s-light .CodeMirror-linenumber {
  color: #839496;
}

/* Common */
.cm-s-solarized .CodeMirror-linenumber {
  padding: 0 5px;
}
.cm-s-solarized .CodeMirror-guttermarker-subtle { color: #586e75; }
.cm-s-solarized.cm-s-dark .CodeMirror-guttermarker { color: #ddd; }
.cm-s-solarized.cm-s-light .CodeMirror-guttermarker { color: #cb4b16; }

.cm-s-solarized .CodeMirror-gutter .CodeMirror-gutter-text {
  color: #586e75;
}

/* Cursor */
.cm-s-solarized .CodeMirror-cursor { border-left: 1px solid #819090; }

/* Fat cursor */
.cm-s-solarized.cm-s-light.cm-fat-cursor .CodeMirror-cursor { background: #77ee77; }
.cm-s-solarized.cm-s-light .cm-animate-fat-cursor { background-color: #77ee77; }
.cm-s-solarized.cm-s-dark.cm-fat-cursor .CodeMirror-cursor { background: #586e75; }
.cm-s-solarized.cm-s-dark .cm-animate-fat-cursor { background-color: #586e75; }

/* Active line */
.cm-s-solarized.cm-s-dark .CodeMirror-activeline-background {
  background: rgba(255, 255, 255, 0.06);
}
.cm-s-solarized.cm-s-light .CodeMirror-activeline-background {
  background: rgba(0, 0, 0, 0.06);
}

.cm-s-the-matrix.CodeMirror { background: #000000; color: #00FF00; }
.cm-s-the-matrix div.CodeMirror-selected { background: #2D2D2D; }
.cm-s-the-matrix .CodeMirror-line::selection, .cm-s-the-matrix .CodeMirror-line > span::selection, .cm-s-the-matrix .CodeMirror-line > span > span::selection { background: rgba(45, 45, 45, 0.99); }
.cm-s-the-matrix .CodeMirror-line::-moz-selection, .cm-s-the-matrix .CodeMirror-line > span::-moz-selection, .cm-s-the-matrix .CodeMirror-line > span > span::-moz-selection { background: rgba(45, 45, 45, 0.99); }
.cm-s-the-matrix .CodeMirror-gutters { background: #060; border-right: 2px solid #00FF00; }
.cm-s-the-matrix .CodeMirror-guttermarker { color: #0f0; }
.cm-s-the-matrix .CodeMirror-guttermarker-subtle { color: white; }
.cm-s-the-matrix .CodeMirror-linenumber { color: #FFFFFF; }
.cm-s-the-matrix .CodeMirror-cursor { border-left: 1px solid #00FF00; }

.cm-s-the-matrix span.cm-keyword { color: #008803; font-weight: bold; }
.cm-s-the-matrix span.cm-atom { color: #3FF; }
.cm-s-the-matrix span.cm-number { color: #FFB94F; }
.cm-s-the-matrix span.cm-def { color: #99C; }
.cm-s-the-matrix span.cm-variable { color: #F6C; }
.cm-s-the-matrix span.cm-variable-2 { color: #C6F; }
.cm-s-the-matrix span.cm-variable-3, .cm-s-the-matrix span.cm-type { color: #96F; }
.cm-s-the-matrix span.cm-property { color: #62FFA0; }
.cm-s-the-matrix span.cm-operator { color: #999; }
.cm-s-the-matrix span.cm-comment { color: #CCCCCC; }
.cm-s-the-matrix span.cm-string { color: #39C; }
.cm-s-the-matrix span.cm-meta { color: #C9F; }
.cm-s-the-matrix span.cm-qualifier { color: #FFF700; }
.cm-s-the-matrix span.cm-builtin { color: #30a; }
.cm-s-the-matrix span.cm-bracket { color: #cc7; }
.cm-s-the-matrix span.cm-tag { color: #FFBD40; }
.cm-s-the-matrix span.cm-attribute { color: #FFF700; }
.cm-s-the-matrix span.cm-error { color: #FF0000; }

.cm-s-the-matrix .CodeMirror-activeline-background { background: #040; }

/*
Copyright (C) 2011 by MarkLogic Corporation
Author: Mike Brevoort <mike@brevoort.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/
.cm-s-xq-light span.cm-keyword { line-height: 1em; font-weight: bold; color: #5A5CAD; }
.cm-s-xq-light span.cm-atom { color: #6C8CD5; }
.cm-s-xq-light span.cm-number { color: #164; }
.cm-s-xq-light span.cm-def { text-decoration:underline; }
.cm-s-xq-light span.cm-variable { color: black; }
.cm-s-xq-light span.cm-variable-2 { color:black; }
.cm-s-xq-light span.cm-variable-3, .cm-s-xq-light span.cm-type { color: black; }
.cm-s-xq-light span.cm-property {}
.cm-s-xq-light span.cm-operator {}
.cm-s-xq-light span.cm-comment { color: #0080FF; font-style: italic; }
.cm-s-xq-light span.cm-string { color: red; }
.cm-s-xq-light span.cm-meta { color: yellow; }
.cm-s-xq-light span.cm-qualifier { color: grey; }
.cm-s-xq-light span.cm-builtin { color: #7EA656; }
.cm-s-xq-light span.cm-bracket { color: #cc7; }
.cm-s-xq-light span.cm-tag { color: #3F7F7F; }
.cm-s-xq-light span.cm-attribute { color: #7F007F; }
.cm-s-xq-light span.cm-error { color: #f00; }

.cm-s-xq-light .CodeMirror-activeline-background { background: #e8f2ff; }
.cm-s-xq-light .CodeMirror-matchingbracket { outline:1px solid grey;color:black !important;background:yellow; }

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.CodeMirror {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;
  /* Changed to auto to autogrow */
}

.CodeMirror pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* This causes https://github.com/jupyter/jupyterlab/issues/522 */
/* May not cause it not because we changed it! */
.CodeMirror-lines {
  padding: var(--jp-code-padding) 0;
}

.CodeMirror-linenumber {
  padding: 0 8px;
}

.jp-CodeMirrorEditor-static {
  margin: var(--jp-code-padding);
}

.jp-CodeMirrorEditor,
.jp-CodeMirrorEditor-static {
  cursor: text;
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.CodeMirror.jp-mod-readOnly .CodeMirror-cursor {
  display: none;
}

.CodeMirror-gutters {
  border-right: 1px solid var(--jp-border-color2);
  background-color: var(--jp-layout-color0);
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.CodeMirror-selectedtext.cm-searching {
  background-color: var(--jp-search-selected-match-background-color) !important;
  color: var(--jp-search-selected-match-color) !important;
}

.cm-searching {
  background-color: var(
    --jp-search-unselected-match-background-color
  ) !important;
  color: var(--jp-search-unselected-match-color) !important;
}

.CodeMirror-focused .CodeMirror-selected {
  background-color: var(--jp-editor-selected-focused-background);
}

.CodeMirror-selected {
  background-color: var(--jp-editor-selected-background);
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/**
 * Here is our jupyter theme for CodeMirror syntax highlighting
 * This is used in our marked.js syntax highlighting and CodeMirror itself
 * The string "jupyter" is set in ../codemirror/widget.DEFAULT_CODEMIRROR_THEME
 * This came from the classic notebook, which came form highlight.js/GitHub
 */

/**
 * CodeMirror themes are handling the background/color in this way. This works
 * fine for CodeMirror editors outside the notebook, but the notebook styles
 * these things differently.
 */
.CodeMirror.cm-s-jupyter {
  background: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* In the notebook, we want this styling to be handled by its container */
.jp-CodeConsole .CodeMirror.cm-s-jupyter,
.jp-Notebook .CodeMirror.cm-s-jupyter {
  background: transparent;
}

.cm-s-jupyter .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}
.cm-s-jupyter span.cm-keyword {
  color: var(--jp-mirror-editor-keyword-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-atom {
  color: var(--jp-mirror-editor-atom-color);
}
.cm-s-jupyter span.cm-number {
  color: var(--jp-mirror-editor-number-color);
}
.cm-s-jupyter span.cm-def {
  color: var(--jp-mirror-editor-def-color);
}
.cm-s-jupyter span.cm-variable {
  color: var(--jp-mirror-editor-variable-color);
}
.cm-s-jupyter span.cm-variable-2 {
  color: var(--jp-mirror-editor-variable-2-color);
}
.cm-s-jupyter span.cm-variable-3 {
  color: var(--jp-mirror-editor-variable-3-color);
}
.cm-s-jupyter span.cm-punctuation {
  color: var(--jp-mirror-editor-punctuation-color);
}
.cm-s-jupyter span.cm-property {
  color: var(--jp-mirror-editor-property-color);
}
.cm-s-jupyter span.cm-operator {
  color: var(--jp-mirror-editor-operator-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-comment {
  color: var(--jp-mirror-editor-comment-color);
  font-style: italic;
}
.cm-s-jupyter span.cm-string {
  color: var(--jp-mirror-editor-string-color);
}
.cm-s-jupyter span.cm-string-2 {
  color: var(--jp-mirror-editor-string-2-color);
}
.cm-s-jupyter span.cm-meta {
  color: var(--jp-mirror-editor-meta-color);
}
.cm-s-jupyter span.cm-qualifier {
  color: var(--jp-mirror-editor-qualifier-color);
}
.cm-s-jupyter span.cm-builtin {
  color: var(--jp-mirror-editor-builtin-color);
}
.cm-s-jupyter span.cm-bracket {
  color: var(--jp-mirror-editor-bracket-color);
}
.cm-s-jupyter span.cm-tag {
  color: var(--jp-mirror-editor-tag-color);
}
.cm-s-jupyter span.cm-attribute {
  color: var(--jp-mirror-editor-attribute-color);
}
.cm-s-jupyter span.cm-header {
  color: var(--jp-mirror-editor-header-color);
}
.cm-s-jupyter span.cm-quote {
  color: var(--jp-mirror-editor-quote-color);
}
.cm-s-jupyter span.cm-link {
  color: var(--jp-mirror-editor-link-color);
}
.cm-s-jupyter span.cm-error {
  color: var(--jp-mirror-editor-error-color);
}
.cm-s-jupyter span.cm-hr {
  color: #999;
}

.cm-s-jupyter span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}

.cm-s-jupyter .CodeMirror-activeline-background,
.cm-s-jupyter .CodeMirror-gutter {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0px;
  padding: 0px;
  line-height: normal;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}
.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}
.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
}
.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
}
.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}
.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}
.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0em;
}

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: 12px;
  table-layout: fixed;
  margin-left: auto;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon table {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0px;
}

.jp-RenderedHTMLCommon p {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}
/* ...or leave it untouched if they don't */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-dark-background {
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-light-background {
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}
.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}
.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}
.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}
.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}
.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}
.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}
.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}
.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: 0.8em;
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser {
  display: flex;
  flex-direction: column;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  border-bottom: none;
  height: auto;
  margin: var(--jp-toolbar-header-margin);
  box-shadow: none;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 4px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0px 2px;
  padding: 0px 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0px;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar.jp-Toolbar {
  padding: 0px;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  justify-content: space-evenly;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-Toolbar-item {
  flex: 1;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-ToolbarButtonComponent {
  width: 100%;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px 12px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-item.jp-mod-selected {
  color: white;
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon:before {
  color: limegreen;
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0px;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-DirListing-deadSpace {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

.jp-FileDialog.jp-mod-conflict input {
  color: red;
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
}

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: flex;
  flex-direction: row;
}

.jp-OutputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-output {
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea-child .jp-OutputArea-output {
  flex-grow: 1;
  flex-shrink: 1;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0px;
  padding: 0px;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0px;
  flex: 1 1 auto;
}

.jp-OutputArea-executeResult.jp-RenderedText {
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-OutputArea-stdin {
  line-height: var(--jp-code-line-height);
  padding-top: var(--jp-code-padding);
  display: flex;
}

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;
  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0px;
  bottom: 0px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0px;
  width: 100%;
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: flex;
  flex-direction: row;
}

.jp-InputArea-editor {
  flex: 1 1 auto;
}

.jp-InputArea-editor {
  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0px;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: flex;
  flex-direction: row;
  flex: 1 1 auto;
}

.jp-Placeholder-prompt {
  box-sizing: border-box;
}

.jp-Placeholder-content {
  flex: 1 1 auto;
  border: none;
  background: transparent;
  height: 20px;
  box-sizing: border-box;
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0px;
  margin: 0px;
  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 200px;
  box-shadow: inset 0 0 6px 2px rgba(0, 0, 0, 0.3);
  margin-left: var(--jp-private-cell-scrolling-output-offset);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  flex: 0 0
    calc(
      var(--jp-cell-prompt-width) -
        var(--jp-private-cell-scrolling-output-offset)
    );
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  flex: 1 1 auto;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: 2px;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: flex;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0px;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-NotebookTools-tool {
  padding: 0px 12px 0 12px;
}

.jp-ActiveCellTool {
  padding: 12px;
  background-color: var(--jp-layout-color1);
  border-top: none !important;
}

.jp-ActiveCellTool .jp-InputArea-prompt {
  flex: 0 0 auto;
  padding-left: 0px;
}

.jp-ActiveCellTool .jp-InputArea-editor {
  flex: 1 1 auto;
  background: var(--jp-cell-editor-background);
  border-color: var(--jp-cell-editor-border-color);
}

.jp-ActiveCellTool .jp-InputArea-editor .CodeMirror {
  background: transparent;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0px 12px 0px;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label {
  line-height: 1.4;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensurePackage() in @jupyterlab/buildutils */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

</style>

    <style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0px 2px 1px -1px var(--jp-shadow-umbra-color),
    0px 1px 1px 0px var(--jp-shadow-penumbra-color),
    0px 1px 3px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0px 3px 1px -2px var(--jp-shadow-umbra-color),
    0px 2px 2px 0px var(--jp-shadow-penumbra-color),
    0px 1px 5px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0px 2px 4px -1px var(--jp-shadow-umbra-color),
    0px 4px 5px 0px var(--jp-shadow-penumbra-color),
    0px 1px 10px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0px 3px 5px -1px var(--jp-shadow-umbra-color),
    0px 6px 10px 0px var(--jp-shadow-penumbra-color),
    0px 1px 18px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0px 5px 5px -3px var(--jp-shadow-umbra-color),
    0px 8px 10px 1px var(--jp-shadow-penumbra-color),
    0px 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0px 7px 8px -4px var(--jp-shadow-umbra-color),
    0px 12px 17px 2px var(--jp-shadow-penumbra-color),
    0px 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0px 8px 10px -5px var(--jp-shadow-umbra-color),
    0px 16px 24px 2px var(--jp-shadow-penumbra-color),
    0px 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0px 10px 13px -6px var(--jp-shadow-umbra-color),
    0px 20px 31px 3px var(--jp-shadow-penumbra-color),
    0px 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0px 11px 15px -7px var(--jp-shadow-umbra-color),
    0px 24px 38px 3px var(--jp-shadow-penumbra-color),
    0px 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;

  --jp-ui-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica,
    Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;

  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);

  --jp-content-link-color: var(--md-blue-700);

  --jp-content-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: Menlo, Consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-700);
  --jp-brand-color1: var(--md-blue-500);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);

  --jp-accent-color0: var(--md-green-700);
  --jp-accent-color1: var(--md-green-500);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-700);
  --jp-warn-color1: var(--md-orange-500);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-700);
  --jp-error-color1: var(--md-red-500);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-700);
  --jp-success-color1: var(--md-green-500);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-700);
  --jp-info-color1: var(--md-cyan-500);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;

  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;

  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);

  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: 'Source Code Pro', monospace;
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-border-color1);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: #05a;
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #aa22ff;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #aa22ff;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 180px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);
}
</style>

<style type="text/css">
a.anchor-link {
   display: none;
}
.highlight  {
    margin: 0.4em;
}

/* Input area styling */
.jp-InputArea {
    overflow: hidden;
}

.jp-InputArea-editor {
    overflow: hidden;
}

@media print {
  body {
    margin: 0;
  }
}
</style>



<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-MML-AM_CHTML-full,Safe"> </script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: { 
                    automatic: true 
                    }
                },
                "HTML-CSS": {
                    linebreaks: { 
                    automatic: true 
                    }
                }
            });
        
            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
    <!-- End of mathjax configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">

<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Import-packages-and-setup-display-options">Import packages and setup display options<a class="anchor-link" href="#Import-packages-and-setup-display-options">&#182;</a></h2>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[1]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="n">pd</span><span class="o">.</span><span class="n">set_option</span><span class="p">(</span><span class="s1">&#39;display.max_rows&#39;</span><span class="p">,</span> <span class="mi">500</span><span class="p">)</span>
<span class="n">pd</span><span class="o">.</span><span class="n">set_option</span><span class="p">(</span><span class="s1">&#39;display.max_columns&#39;</span><span class="p">,</span> <span class="mi">500</span><span class="p">)</span>
<span class="n">pd</span><span class="o">.</span><span class="n">set_option</span><span class="p">(</span><span class="s1">&#39;display.width&#39;</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="o">%</span><span class="k">matplotlib</span> inline
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="n">sns</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">rc</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;figure.figsize&#39;</span><span class="p">:(</span><span class="mi">15</span><span class="p">,</span><span class="mi">12</span><span class="p">)})</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Import-business-data-from-Yelp-Academic-Dataset">Import business data from Yelp Academic Dataset<a class="anchor-link" href="#Import-business-data-from-Yelp-Academic-Dataset">&#182;</a></h2>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[3]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;yelp_academic_dataset_business.csv&#39;</span><span class="p">)</span>
<span class="n">business_data</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[3]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>attributes</th>
      <th>attributes.AcceptsInsurance</th>
      <th>attributes.AgesAllowed</th>
      <th>attributes.Alcohol</th>
      <th>attributes.Ambience</th>
      <th>attributes.BYOB</th>
      <th>attributes.BYOBCorkage</th>
      <th>attributes.BestNights</th>
      <th>attributes.BikeParking</th>
      <th>attributes.BusinessAcceptsBitcoin</th>
      <th>attributes.BusinessAcceptsCreditCards</th>
      <th>attributes.BusinessParking</th>
      <th>attributes.ByAppointmentOnly</th>
      <th>attributes.Caters</th>
      <th>attributes.CoatCheck</th>
      <th>attributes.Corkage</th>
      <th>attributes.DietaryRestrictions</th>
      <th>attributes.DogsAllowed</th>
      <th>attributes.DriveThru</th>
      <th>attributes.GoodForDancing</th>
      <th>attributes.GoodForKids</th>
      <th>attributes.GoodForMeal</th>
      <th>attributes.HairSpecializesIn</th>
      <th>attributes.HappyHour</th>
      <th>attributes.HasTV</th>
      <th>attributes.Music</th>
      <th>attributes.NoiseLevel</th>
      <th>attributes.Open24Hours</th>
      <th>attributes.OutdoorSeating</th>
      <th>attributes.RestaurantsAttire</th>
      <th>attributes.RestaurantsCounterService</th>
      <th>attributes.RestaurantsDelivery</th>
      <th>attributes.RestaurantsGoodForGroups</th>
      <th>attributes.RestaurantsPriceRange2</th>
      <th>attributes.RestaurantsReservations</th>
      <th>attributes.RestaurantsTableService</th>
      <th>attributes.RestaurantsTakeOut</th>
      <th>attributes.Smoking</th>
      <th>attributes.WheelchairAccessible</th>
      <th>attributes.WiFi</th>
      <th>business_id</th>
      <th>categories</th>
      <th>city</th>
      <th>hours</th>
      <th>hours.Friday</th>
      <th>hours.Monday</th>
      <th>hours.Saturday</th>
      <th>hours.Sunday</th>
      <th>hours.Thursday</th>
      <th>hours.Tuesday</th>
      <th>hours.Wednesday</th>
      <th>is_open</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>name</th>
      <th>neighborhood</th>
      <th>postal_code</th>
      <th>review_count</th>
      <th>stars</th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1314 44 Avenue NE</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>True</td>
      <td>{'garage': False, 'street': True, 'validated':...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>average</td>
      <td>NaN</td>
      <td>False</td>
      <td>casual</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>2.0</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Apn5Q_b6Nz61Tq4XzPdf9A</td>
      <td>Tours, Breweries, Pizza, Restaurants, Food, Ho...</td>
      <td>Calgary</td>
      <td>NaN</td>
      <td>11:0-21:0</td>
      <td>8:30-17:0</td>
      <td>11:0-21:0</td>
      <td>NaN</td>
      <td>11:0-21:0</td>
      <td>11:0-21:0</td>
      <td>11:0-21:0</td>
      <td>1</td>
      <td>51.091813</td>
      <td>-114.031675</td>
      <td>Minhas Micro Brewery</td>
      <td>NaN</td>
      <td>T2E 6L6</td>
      <td>24</td>
      <td>4.0</td>
      <td>AB</td>
    </tr>
    <tr>
      <th>1</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>none</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>True</td>
      <td>{'garage': False, 'street': True, 'validated':...</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>False</td>
      <td>NaN</td>
      <td>True</td>
      <td>{'dessert': False, 'latenight': False, 'lunch'...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>casual</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>2.0</td>
      <td>False</td>
      <td>False</td>
      <td>True</td>
      <td>NaN</td>
      <td>True</td>
      <td>no</td>
      <td>AjEbIBw6ZFfln7ePHha9PA</td>
      <td>Chicken Wings, Burgers, Caterers, Street Vendo...</td>
      <td>Henderson</td>
      <td>NaN</td>
      <td>17:0-23:0</td>
      <td>NaN</td>
      <td>17:0-23:0</td>
      <td>17:0-23:0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>35.960734</td>
      <td>-114.939821</td>
      <td>CK'S BBQ &amp; Catering</td>
      <td>NaN</td>
      <td>89002</td>
      <td>3</td>
      <td>4.5</td>
      <td>NV</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1335 rue Beaubien E</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>beer_and_wine</td>
      <td>{'romantic': False, 'intimate': False, 'classy...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>False</td>
      <td>{'garage': False, 'street': False, 'validated'...</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>{'dessert': False, 'latenight': False, 'lunch'...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>average</td>
      <td>NaN</td>
      <td>False</td>
      <td>casual</td>
      <td>NaN</td>
      <td>False</td>
      <td>True</td>
      <td>2.0</td>
      <td>True</td>
      <td>True</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>free</td>
      <td>O8S5hYJ1SMc8fA4QBtVujA</td>
      <td>Breakfast &amp; Brunch, Restaurants, French, Sandw...</td>
      <td>Montréal</td>
      <td>NaN</td>
      <td>10:0-22:0</td>
      <td>10:0-22:0</td>
      <td>10:0-22:0</td>
      <td>10:0-22:0</td>
      <td>10:0-22:0</td>
      <td>10:0-22:0</td>
      <td>10:0-22:0</td>
      <td>0</td>
      <td>45.540503</td>
      <td>-73.599300</td>
      <td>La Bastringue</td>
      <td>Rosemont-La Petite-Patrie</td>
      <td>H2G 1K7</td>
      <td>5</td>
      <td>4.0</td>
      <td>QC</td>
    </tr>
    <tr>
      <th>3</th>
      <td>211 W Monroe St</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>bFzdJJ3wp3PZssNEsyU23g</td>
      <td>Insurance, Financial Services</td>
      <td>Phoenix</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>33.449999</td>
      <td>-112.076979</td>
      <td>Geico Insurance</td>
      <td>NaN</td>
      <td>85003</td>
      <td>8</td>
      <td>1.5</td>
      <td>AZ</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2005 Alyth Place SE</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8USyCYqpScwiNEb58Bt6CA</td>
      <td>Home &amp; Garden, Nurseries &amp; Gardening, Shopping...</td>
      <td>Calgary</td>
      <td>NaN</td>
      <td>8:0-17:0</td>
      <td>8:0-17:0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8:0-17:0</td>
      <td>8:0-17:0</td>
      <td>8:0-17:0</td>
      <td>1</td>
      <td>51.035591</td>
      <td>-114.027366</td>
      <td>Action Engine</td>
      <td>NaN</td>
      <td>T2H 0N5</td>
      <td>4</td>
      <td>2.0</td>
      <td>AB</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Clean-business-data">Clean business data<a class="anchor-link" href="#Clean-business-data">&#182;</a></h3>
</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Check for columns that have missing values and drop those that ONLY have them</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[4]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">sns</span><span class="o">.</span><span class="n">heatmap</span><span class="p">(</span><span class="n">business_data</span><span class="o">.</span><span class="n">isnull</span><span class="p">(),</span> <span class="n">cbar</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[4]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>&lt;AxesSubplot:&gt;</pre>
</div>

</div>

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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3br88ssvREVF0a5dOwB8fHxMzqcHGTRoEO+99x7Xrl1j586dTJ06lXHjxvH5558XWjZL65Jx48Zx8uRJ0tLSqFmzpnF5bm4utWrVKrSuU3punzx5Ej8/P27fvk1cXByvvfYaCxYsoFmzZg9cP39/eXl5mVz3DQYDdnZ2nDx58qF5zL/m//333/z5558888wz2Nvb89NPP9GoUaOHllGn05GTk8Pw4cMZMWIE//nPf8jOziYqKqrAfRIcHMzBgweN1xlLA5mi1nf5srKy2LVrF1u2bOHq1av069ePl19+ucDGjc2bN7NlyxYyMzPp27evxY0hStMdOnSILVu2mFx/C9svw4YN4++//y7SdvIpud4rTafkHuj7779n2rRp5ObmEhcXR+/evZk7dy7t27cvcFs7duxg2bJlZGVlERcXx8svv0xAQAB9+/YtMF1RzrcuXboUeG9d2DVRSZ2cXw/lN7rkK6weKkp9fD+l+9GEoQzo37+/wWAwGGbPnm1Yvny5ybKH8fHxMaSlpRk++eQTw/Tp0w05OTkGHx+fQrfVt29fQ15enqFv374Gg8FgyMnJMfTs2fOh6x88eNBw8OBBwwcffGCYMmWK4fDhw4affvrJEBYWZggJCbGwhAbDjRs3DNevX7do3b59+xru3LljzKNery8wj7169TLcvHnTkJGRYWjVqpVBr9cbDAaD4e7du4bevXtbtL2i7BODQdlvZjAYDB988IHhm2++MX7eu3evISgoyPDrr78aXn311Yem6927tyE2Ntbwww8/GH+TgwcPFrq9AQMGGAwGg2Hy5MmGuLg4g8FgKPQ4CQsLM6xevdpw48YNw40bNwzr1q0zBAUFGb7++mvDG2+8Ueg2s7KyDJs3bzZ06NDB0LFjR4OPj4/hp59+KtE85lu8eLGhSZMmhk2bNlm0/vDhww3ffvutoV+/foa8vDxDXFycYciQIYWm69+/v+HkyZOG+Ph4Q0BAgEGv11uUx9dee81w9epV4+e///7bMHToUIvymi8vL6/AYyOf0mNLadkelM8///yzwHVefPFFk/1hqaCgoAf+s8TPP/9smDFjhqFz586G4OBgw9GjRwtc39vb23Dz5k3j51u3bllUj+T7+++/LV7XYPi/4z80NNTwySefGAwGy47/V1991aROvXHjhmHo0KGGnJwcQ58+fR6YRkldd39+8tMZDIaHbuNhvv76a0OHDh0M//73vw0zZ840ZGZmFri9rKwsw/Llyw2zZs0yycP/6t27t+HWrVsGg8FgOHr0qOE///mP4fDhw2b5fZj8/T9x4kTD5s2bLU5XlLrkxo0bhgsXLhjGjBljuHjxovHf5cuXDTk5OYVuS+m5PWTIEMPZs2eN5fnuu++M5X1URo4caUhJSTF+vnjxomH48OEPXd/Hx8eQl5dnWLRokWHRokUGg8Gya6nBcO9as2XLFsPIkSMNPj4+hlWrVhkyMjIKTFMS9V3+sdyqVSvD2LFjTcr7IKmpqYYVK1YYunTpYhg1apTJb/ko0uVfgzt27Gjw9vY2rF692nDnzp2Hrn/x4kXDkiVLDL179zaMGjXKsHPnTkN2dnaRtmXp9V5pOiX3QK+88oohPT3dePz/9ttvFtVb/fr1M9y4ccOYLi0tzdCrV69C0xXlfLt48aLhwoULhqCgIMOSJUsMly5dMqSnpxs++ugjw4wZMwrdlpI6WWk9VJT6+H5K9+P9ysQzgbm5uWRmZrJ79246derElStXuHPnTqHpatSowb59++jUqROOjo4Wpcnvvs1vgcjOzi6wS/ff//63sXdt5syZtG7dmlatWhESEsKvv/5a6PYuXLjAK6+8wosvvkjXrl3p168fKSkphebx/iECLi4uODg4PHR9R0dHypUrR9WqValbty5ubm4AODg44OjoWGgei7pPQPlv9ttvvxlb7uFeC+/p06dp2rRpgeldXV157bXXaNOmjfE3+fe//13o9hwcHNi1axd79+6lU6dO7N69u9CyHT16lDfffBN3d3fc3d0ZMmQIp0+fplu3bly/fv2h6b7//nsCAwPp1q0bR44cYf78+ezdu5eIiAjee++9EstjcHCw8d9ff/1F5cqViY+PNy4ryLVr12jfvr2xZXvQoEHo9foC0+Tz8vJi7969dOnSBTc3N3JycgpNk56ebtLr9dhjjxX5mYhz586Rnp5e6HpKjy1QVra4uDieeeYZmjRpQpMmTWjatCnDhw8vME3t2rUVDZOJiIh44D9LtGzZkmnTprF161YcHR157bXXClw/JyfHpP4prNcq36lTp+jRowd9+/YlLS2Nbt26WVRH5uXlkZyczO7du+ncuTMnT5606JnGa9euGes6uFdPXr9+HUdHx4e2MCup6+DeOXrjxg1jupSUFIvS3bx5ky+++II33niDuXPnMnjwYDZt2sQTTzzx0JEdcG+fuLq6smfPHjp27EheXh5ZWVkPXf+xxx4D4JlnnmH+/Pm8//77nDlzpsCW9vvTfvzxx/zwww907tyZTz/91GS/PkxR6hJ3d3c8PT0ZPnw4qampxn9//vknP/30U6HbUnpuZ2Vl8eSTTxo/5/eyPczkyZON/y/sOv0wqampJsOn69SpQ2pq6kPXz83NJS8vj8TERDp06EBWVlaBv/X9XF1d8fDwoHbt2uj1ek6fPs2bb77J2rVrC0ynpL77448/WLx4Md27d2f9+vVMmjSJH374gVdffZW33377oekuXLjAF198webNm6lXrx7dunVj586dhY7sUJru4MGDhIaGMn/+fF544QWmTJnC1atXGTt27EPTeHh40K9fP/r06cNvv/1GbGwsvXv35ptvvnloGqXXe6XplNwD5eXlmfRsNmzYsMD189nb25sMEa5Ro4ZF9V1RzjcPDw88PT05ffo077zzDrVq1aJ69eoMHz6cn3/+udBtKamT8+uhZcuWcevWLS5dumRRPVTU+jif0v14v8Lv4DVgxIgRDBo0iC5dutCoUSO6d+/OhAkTCkzTsGFDRo8ezcWLF2nXrh3vv/++RcMhevTowfvvv8/169dZs2YNCQkJ9O7du9B0d+7c4ffff6d+/foAnD59mrt37xaabtq0aYwcOZIePXoA97qHp06dWuBQp3//+9/MmjWLrKwsdu/eTVxcHG3btn3o+vcfVAUFiw/zv/tk69athe6TkSNHFvk3A6hQoQKfffYZL7/8Mnl5eWzbto2KFSty7tw58vLyHpquffv2xMbG0r59e1xcXIzLC3uWKjQ0lDVr1jBt2jRq1KjBl19+ycyZMwtMY29vz7fffssLL7wAwLfffouzszMZGRkF/ubR0dG88sorTJ8+3XhTBtC4ceMCg4Oi5vF/K35LguF8rq6uXL582VhxHjlyxKJnEqpVq0ZYWBjJycnMmTOHyMjIQvc93HuO5K233uKll17CYDCwc+dOevbsWWCa+4diGQwGqlSpwgcffFDotpQeW0rLtnz5chISEliwYAF+fn7s27ePH3/8scA0TzzxBEOGDKFNmzYm+72w5wgfNnSmsCEzBoOB//73v2zfvp3vv/+eDh06sH79+gLTdO3alTfeeIOePXtiZ2fHrl276NKlS4FpAMLCwliyZAkffPABNWvWZPr06eh0OjZt2lRgOn9/f2bPns3w4cOpW7cugwYNKrQxA+4N287PZ15eHl9//TUvvvgiW7ZseeiQLiV1Hdwbejps2DAuXbrEO++8w88//8yHH35YaLoXX3yRzp07M27cOJNnwoYMGVLgs7vt2rWjd+/euLq68txzz/Haa6899Dd49tln8fPz491336Vhw4Y899xzTJs2jbfeesuiYDoqKoqNGzeyePFiKlasSFpaGvPmzSs0nZK6ZNGiRcb/3717l9OnT9O6detCn3lXem5XqlSJU6dOGfO4devWAhthTpw4Yfy/n59foUNpH6RZs2YEBgbSs2dPDAYD27Zto3Xr1g9dv1+/frRv355nnnmGli1b0qtXr4cOvb7f/Pnz2b59O56engwYMIApU6bg4uKCXq/nxRdffGhjj9L67q233qJ///58/PHHJo9EdOzYkQMHDjwwzeDBg8nIyKBv376sWrXKuJ1+/foV+Myp0nSdO3c27o9p06YZh863adOGAQMGPDDNxo0bSUhI4MqVK/Tr14/169dTq1Yt0tLS8PHxoVu3bg9MFx0dzYABA4p8vVeaTsk9UK1atdizZw92dnb8888/rFu3zqLf+qmnnmLt2rXcvXuXkydPsn79ery8vApNV9TzLd/3339vHMK+b98+i+5jldbJcO+eKykpyeT5vIIe0ypKfXw/pfvxfmXimcD7WTrJy927d41j7StWrEhSUhIdOnSwqOfr22+/5b///S95eXm0a9eOTp06FZrmu+++IygoiJo1a2IwGLh69Spz584tsHKHe5XW/05g0KdPH7Zt2/bQNHl5ecTHx5vk8dVXX31o2Z5++mmaN2+OwWAgOTnZOLbcYDDw66+/FnpjCqb7pG3btoVOJnDgwAH+85//GD/n5uaSmJjISy+9VGC6tLQ0wsPDOXDgAA4ODjz//PNMnjyZXbt2Ua9evYdW8A864Qp6lqqgllcouOI8c+YMQUFB/PXXXwA8/vjjREZG8tVXX1GnTh18fHxKbFtwrxHko48+KnCdB9Hr9SQkJDB06FDS0tL47LPPGDVqlMmF5X8dP36cqVOn8ueff/L4449z/fp1FixYQKtWrQrd1u7du3n66aepV68e69atMz6LW5hdu3Zx6NAh7OzsaNeuHS+++GKB6586darIFSUoP7aUlm3gwIFs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
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[5]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">axis</span> <span class="o">=</span> <span class="s1">&#39;columns&#39;</span><span class="p">,</span> <span class="n">how</span> <span class="o">=</span> <span class="s1">&#39;all&#39;</span><span class="p">,</span> <span class="n">inplace</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">business_data</span><span class="o">.</span><span class="n">shape</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[5]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>(188593, 59)</pre>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Chang the format of column names</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="n">business_data</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s1">&#39;.&#39;</span><span class="p">,</span> <span class="s1">&#39;_&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<span class="n">business_data</span><span class="o">.</span><span class="n">columns</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[6]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>Index([&#39;address&#39;, &#39;attributes_acceptsinsurance&#39;, &#39;attributes_agesallowed&#39;, &#39;attributes_alcohol&#39;,
       &#39;attributes_ambience&#39;, &#39;attributes_byob&#39;, &#39;attributes_byobcorkage&#39;, &#39;attributes_bestnights&#39;,
       &#39;attributes_bikeparking&#39;, &#39;attributes_businessacceptsbitcoin&#39;,
       &#39;attributes_businessacceptscreditcards&#39;, &#39;attributes_businessparking&#39;,
       &#39;attributes_byappointmentonly&#39;, &#39;attributes_caters&#39;, &#39;attributes_coatcheck&#39;,
       &#39;attributes_corkage&#39;, &#39;attributes_dietaryrestrictions&#39;, &#39;attributes_dogsallowed&#39;,
       &#39;attributes_drivethru&#39;, &#39;attributes_goodfordancing&#39;, &#39;attributes_goodforkids&#39;,
       &#39;attributes_goodformeal&#39;, &#39;attributes_hairspecializesin&#39;, &#39;attributes_happyhour&#39;,
       &#39;attributes_hastv&#39;, &#39;attributes_music&#39;, &#39;attributes_noiselevel&#39;, &#39;attributes_open24hours&#39;,
       &#39;attributes_outdoorseating&#39;, &#39;attributes_restaurantsattire&#39;,
       &#39;attributes_restaurantscounterservice&#39;, &#39;attributes_restaurantsdelivery&#39;,
       &#39;attributes_restaurantsgoodforgroups&#39;, &#39;attributes_restaurantspricerange2&#39;,
       &#39;attributes_restaurantsreservations&#39;, &#39;attributes_restaurantstableservice&#39;,
       &#39;attributes_restaurantstakeout&#39;, &#39;attributes_smoking&#39;, &#39;attributes_wheelchairaccessible&#39;,
       &#39;attributes_wifi&#39;, &#39;business_id&#39;, &#39;categories&#39;, &#39;city&#39;, &#39;hours_friday&#39;, &#39;hours_monday&#39;,
       &#39;hours_saturday&#39;, &#39;hours_sunday&#39;, &#39;hours_thursday&#39;, &#39;hours_tuesday&#39;, &#39;hours_wednesday&#39;,
       &#39;is_open&#39;, &#39;latitude&#39;, &#39;longitude&#39;, &#39;name&#39;, &#39;neighborhood&#39;, &#39;postal_code&#39;, &#39;review_count&#39;,
       &#39;stars&#39;, &#39;state&#39;],
      dtype=&#39;object&#39;)</pre>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Drop not needed columns</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;attributes_acceptsinsurance&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_agesallowed&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_alcohol&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_ambience&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_byob&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_byobcorkage&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_bestnights&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_bikeparking&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_businessacceptsbitcoin&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_businessacceptscreditcards&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_businessparking&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_byappointmentonly&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_caters&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_coatcheck&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_corkage&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_dietaryrestrictions&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_dogsallowed&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_drivethru&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_goodfordancing&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_goodforkids&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_goodformeal&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_hairspecializesin&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_hastv&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_music&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_noiselevel&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_open24hours&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_outdoorseating&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_restaurantsattire&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_restaurantscounterservice&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_restaurantsdelivery&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_restaurantsgoodforgroups&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_restaurantspricerange2&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_restaurantsreservations&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_restaurantstableservice&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_restaurantstakeout&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_smoking&#39;</span><span class="p">,</span> <span class="s1">&#39;attributes_wheelchairaccessible&#39;</span><span class="p">,</span>
       <span class="s1">&#39;attributes_wifi&#39;</span><span class="p">],</span> <span class="n">inplace</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">business_data</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 188593 entries, 0 to 188592
Data columns (total 21 columns):
 #   Column                Non-Null Count   Dtype  
---  ------                --------------   -----  
 0   address               180970 non-null  object 
 1   attributes_happyhour  9285 non-null    object 
 2   business_id           188593 non-null  object 
 3   categories            188052 non-null  object 
 4   city                  188583 non-null  object 
 5   hours_friday          141796 non-null  object 
 6   hours_monday          132761 non-null  object 
 7   hours_saturday        125376 non-null  object 
 8   hours_sunday          93387 non-null   object 
 9   hours_thursday        142359 non-null  object 
 10  hours_tuesday         140607 non-null  object 
 11  hours_wednesday       141843 non-null  object 
 12  is_open               188593 non-null  int64  
 13  latitude              188587 non-null  float64
 14  longitude             188587 non-null  float64
 15  name                  188593 non-null  object 
 16  neighborhood          68655 non-null   object 
 17  postal_code           187912 non-null  object 
 18  review_count          188593 non-null  int64  
 19  stars                 188593 non-null  float64
 20  state                 188593 non-null  object 
dtypes: float64(3), int64(2), object(16)
memory usage: 30.2+ MB
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Remove hours columns</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">columns</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;hours_friday&#39;</span><span class="p">,</span> <span class="s1">&#39;hours_monday&#39;</span><span class="p">,</span> <span class="s1">&#39;hours_saturday&#39;</span><span class="p">,</span> <span class="s1">&#39;hours_sunday&#39;</span><span class="p">,</span> <span class="s1">&#39;hours_thursday&#39;</span><span class="p">,</span> <span class="s1">&#39;hours_tuesday&#39;</span><span class="p">,</span> <span class="s1">&#39;hours_wednesday&#39;</span><span class="p">],</span> <span class="n">inplace</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">business_data</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 188593 entries, 0 to 188592
Data columns (total 14 columns):
 #   Column                Non-Null Count   Dtype  
---  ------                --------------   -----  
 0   address               180970 non-null  object 
 1   attributes_happyhour  9285 non-null    object 
 2   business_id           188593 non-null  object 
 3   categories            188052 non-null  object 
 4   city                  188583 non-null  object 
 5   is_open               188593 non-null  int64  
 6   latitude              188587 non-null  float64
 7   longitude             188587 non-null  float64
 8   name                  188593 non-null  object 
 9   neighborhood          68655 non-null   object 
 10  postal_code           187912 non-null  object 
 11  review_count          188593 non-null  int64  
 12  stars                 188593 non-null  float64
 13  state                 188593 non-null  object 
dtypes: float64(3), int64(2), object(9)
memory usage: 20.1+ MB
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Load-home-prices-index-data-(median-list-price-all-homes-zillow)">Load home prices index data (median list price all homes zillow)<a class="anchor-link" href="#Load-home-prices-index-data-(median-list-price-all-homes-zillow)">&#182;</a></h3>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">home_prices</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">&quot;Metro_mlp_uc_sfrcondo_sm_month.csv&quot;</span><span class="p">)</span>
<span class="n">home_prices</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[9]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>RegionID</th>
      <th>SizeRank</th>
      <th>RegionName</th>
      <th>RegionType</th>
      <th>StateName</th>
      <th>2018-03-31</th>
      <th>2018-04-30</th>
      <th>2018-05-31</th>
      <th>2018-06-30</th>
      <th>2018-07-31</th>
      <th>2018-08-31</th>
      <th>2018-09-30</th>
      <th>2018-10-31</th>
      <th>2018-11-30</th>
      <th>2018-12-31</th>
      <th>2019-01-31</th>
      <th>2019-02-28</th>
      <th>2019-03-31</th>
      <th>2019-04-30</th>
      <th>2019-05-31</th>
      <th>2019-06-30</th>
      <th>2019-07-31</th>
      <th>2019-08-31</th>
      <th>2019-09-30</th>
      <th>2019-10-31</th>
      <th>2019-11-30</th>
      <th>2019-12-31</th>
      <th>2020-01-31</th>
      <th>2020-02-29</th>
      <th>2020-03-31</th>
      <th>2020-04-30</th>
      <th>2020-05-31</th>
      <th>2020-06-30</th>
      <th>2020-07-31</th>
      <th>2020-08-31</th>
      <th>2020-09-30</th>
      <th>2020-10-31</th>
      <th>2020-11-30</th>
      <th>2020-12-31</th>
      <th>2021-01-31</th>
      <th>2021-02-28</th>
      <th>2021-03-31</th>
      <th>2021-04-30</th>
      <th>2021-05-31</th>
      <th>2021-06-30</th>
      <th>2021-07-31</th>
      <th>2021-08-31</th>
      <th>2021-09-30</th>
      <th>2021-10-31</th>
      <th>2021-11-30</th>
      <th>2021-12-31</th>
      <th>2022-01-31</th>
      <th>2022-02-28</th>
      <th>2022-03-31</th>
      <th>2022-04-30</th>
      <th>2022-05-31</th>
      <th>2022-06-30</th>
      <th>2022-07-31</th>
      <th>2022-08-31</th>
      <th>2022-09-30</th>
      <th>2022-10-31</th>
      <th>2022-11-30</th>
      <th>2022-12-31</th>
      <th>2023-01-31</th>
      <th>2023-02-28</th>
      <th>2023-03-31</th>
      <th>2023-04-30</th>
      <th>2023-05-31</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>102001</td>
      <td>0</td>
      <td>United States</td>
      <td>country</td>
      <td>NaN</td>
      <td>263267.0</td>
      <td>271267.0</td>
      <td>276633.0</td>
      <td>280000.0</td>
      <td>280300.0</td>
      <td>279633.0</td>
      <td>279600.0</td>
      <td>279300.0</td>
      <td>278933.0</td>
      <td>277300.0</td>
      <td>275967.0</td>
      <td>276633.0</td>
      <td>281300.0</td>
      <td>287967.0</td>
      <td>294567.0</td>
      <td>297900.0</td>
      <td>298900.0</td>
      <td>297000.0</td>
      <td>294833.0</td>
      <td>292133.0</td>
      <td>290467.0</td>
      <td>287933.0</td>
      <td>284933.0</td>
      <td>285233.0</td>
      <td>289600.0</td>
      <td>295633.0</td>
      <td>299000.0</td>
      <td>303967.0</td>
      <td>309300.0</td>
      <td>314300.0</td>
      <td>315300.0</td>
      <td>315300.0</td>
      <td>313633.0</td>
      <td>309967.0</td>
      <td>304967.0</td>
      <td>307967.0</td>
      <td>314667.0</td>
      <td>326333.0</td>
      <td>333333.0</td>
      <td>339407.0</td>
      <td>341073.0</td>
      <td>340740.0</td>
      <td>339667.0</td>
      <td>339633.0</td>
      <td>338300.0</td>
      <td>333600.0</td>
      <td>330300.0</td>
      <td>335267.0</td>
      <td>346633.0</td>
      <td>362967.0</td>
      <td>376300.0</td>
      <td>387967.0</td>
      <td>393300.0</td>
      <td>393300.0</td>
      <td>391300.0</td>
      <td>386633.0</td>
      <td>381667.0</td>
      <td>375733.0</td>
      <td>371900.0</td>
      <td>371900.0</td>
      <td>374833.0</td>
      <td>383167.0</td>
      <td>391167.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>394913</td>
      <td>1</td>
      <td>New York, NY</td>
      <td>msa</td>
      <td>NY</td>
      <td>503000.0</td>
      <td>513000.0</td>
      <td>521300.0</td>
      <td>526300.0</td>
      <td>528300.0</td>
      <td>526600.0</td>
      <td>526267.0</td>
      <td>527600.0</td>
      <td>529000.0</td>
      <td>527667.0</td>
      <td>524667.0</td>
      <td>524667.0</td>
      <td>528000.0</td>
      <td>537667.0</td>
      <td>544333.0</td>
      <td>549000.0</td>
      <td>547667.0</td>
      <td>544333.0</td>
      <td>544333.0</td>
      <td>545667.0</td>
      <td>549000.0</td>
      <td>549300.0</td>
      <td>549300.0</td>
      <td>549300.0</td>
      <td>552333.0</td>
      <td>555967.0</td>
      <td>559300.0</td>
      <td>561300.0</td>
      <td>566333.0</td>
      <td>574967.0</td>
      <td>584967.0</td>
      <td>592967.0</td>
      <td>597967.0</td>
      <td>599600.0</td>
      <td>596600.0</td>
      <td>594967.0</td>
      <td>594667.0</td>
      <td>597667.0</td>
      <td>598667.0</td>
      <td>595633.0</td>
      <td>589267.0</td>
      <td>579600.0</td>
      <td>574633.0</td>
      <td>574333.0</td>
      <td>576333.0</td>
      <td>576333.0</td>
      <td>576667.0</td>
      <td>584550.0</td>
      <td>592550.0</td>
      <td>603550.0</td>
      <td>610667.0</td>
      <td>617667.0</td>
      <td>613330.0</td>
      <td>606330.0</td>
      <td>599663.0</td>
      <td>606333.0</td>
      <td>612999.0</td>
      <td>619333.0</td>
      <td>619333.0</td>
      <td>624667.0</td>
      <td>634967.0</td>
      <td>647967.0</td>
      <td>662633.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>753899</td>
      <td>2</td>
      <td>Los Angeles, CA</td>
      <td>msa</td>
      <td>CA</td>
      <td>721333.0</td>
      <td>735000.0</td>
      <td>743333.0</td>
      <td>750000.0</td>
      <td>749667.0</td>
      <td>742967.0</td>
      <td>736267.0</td>
      <td>728267.0</td>
      <td>724633.0</td>
      <td>719667.0</td>
      <td>711300.0</td>
      <td>711600.0</td>
      <td>716267.0</td>
      <td>732633.0</td>
      <td>742667.0</td>
      <td>752933.0</td>
      <td>756567.0</td>
      <td>759233.0</td>
      <td>758967.0</td>
      <td>758667.0</td>
      <td>762333.0</td>
      <td>765667.0</td>
      <td>767667.0</td>
      <td>771298.0</td>
      <td>779965.0</td>
      <td>787965.0</td>
      <td>794333.0</td>
      <td>802333.0</td>
      <td>816000.0</td>
      <td>826000.0</td>
      <td>829633.0</td>
      <td>831300.0</td>
      <td>838294.0</td>
      <td>844661.0</td>
      <td>849327.0</td>
      <td>849296.0</td>
      <td>849629.0</td>
      <td>856296.0</td>
      <td>864667.0</td>
      <td>874667.0</td>
      <td>874667.0</td>
      <td>866333.0</td>
      <td>856333.0</td>
      <td>850000.0</td>
      <td>850000.0</td>
      <td>850000.0</td>
      <td>856633.0</td>
      <td>871633.0</td>
      <td>888263.0</td>
      <td>904963.0</td>
      <td>916596.0</td>
      <td>924967.0</td>
      <td>920633.0</td>
      <td>910333.0</td>
      <td>901667.0</td>
      <td>897667.0</td>
      <td>894333.0</td>
      <td>887667.0</td>
      <td>882633.0</td>
      <td>885967.0</td>
      <td>892967.0</td>
      <td>916000.0</td>
      <td>941333.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>394463</td>
      <td>3</td>
      <td>Chicago, IL</td>
      <td>msa</td>
      <td>IL</td>
      <td>284600.0</td>
      <td>294600.0</td>
      <td>300600.0</td>
      <td>302267.0</td>
      <td>301967.0</td>
      <td>297933.0</td>
      <td>296117.0</td>
      <td>292783.0</td>
      <td>288483.0</td>
      <td>283333.0</td>
      <td>280000.0</td>
      <td>284300.0</td>
      <td>291267.0</td>
      <td>301267.0</td>
      <td>306300.0</td>
      <td>309467.0</td>
      <td>306465.0</td>
      <td>302798.0</td>
      <td>298998.0</td>
      <td>295633.0</td>
      <td>290967.0</td>
      <td>284933.0</td>
      <td>281633.0</td>
      <td>284967.0</td>
      <td>291633.0</td>
      <td>297967.0</td>
      <td>299600.0</td>
      <td>301300.0</td>
      <td>304633.0</td>
      <td>307667.0</td>
      <td>309300.0</td>
      <td>306300.0</td>
      <td>303267.0</td>
      <td>298267.0</td>
      <td>296567.0</td>
      <td>299900.0</td>
      <td>304933.0</td>
      <td>309966.0</td>
      <td>311666.0</td>
      <td>313333.0</td>
      <td>313000.0</td>
      <td>307967.0</td>
      <td>302933.0</td>
      <td>299263.0</td>
      <td>295930.0</td>
      <td>289263.0</td>
      <td>284933.0</td>
      <td>287967.0</td>
      <td>297667.0</td>
      <td>309300.0</td>
      <td>317967.0</td>
      <td>323300.0</td>
      <td>324967.0</td>
      <td>322967.0</td>
      <td>319967.0</td>
      <td>314967.0</td>
      <td>308600.0</td>
      <td>302933.0</td>
      <td>299300.0</td>
      <td>302167.0</td>
      <td>308833.0</td>
      <td>319133.0</td>
      <td>329467.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>394514</td>
      <td>4</td>
      <td>Dallas, TX</td>
      <td>msa</td>
      <td>TX</td>
      <td>322997.0</td>
      <td>328497.0</td>
      <td>331797.0</td>
      <td>332800.0</td>
      <td>329502.0</td>
      <td>324202.0</td>
      <td>321168.0</td>
      <td>318966.0</td>
      <td>317633.0</td>
      <td>315999.0</td>
      <td>313333.0</td>
      <td>313667.0</td>
      <td>316967.0</td>
      <td>323633.0</td>
      <td>328467.0</td>
      <td>330133.0</td>
      <td>328467.0</td>
      <td>324966.0</td>
      <td>321633.0</td>
      <td>319933.0</td>
      <td>319600.0</td>
      <td>317967.0</td>
      <td>314667.0</td>
      <td>313633.0</td>
      <td>315267.0</td>
      <td>318600.0</td>
      <td>321633.0</td>
      <td>325633.0</td>
      <td>330600.0</td>
      <td>333233.0</td>
      <td>334267.0</td>
      <td>332633.0</td>
      <td>331600.0</td>
      <td>328600.0</td>
      <td>328559.0</td>
      <td>330293.0</td>
      <td>335926.0</td>
      <td>342633.0</td>
      <td>350967.0</td>
      <td>359667.0</td>
      <td>367829.0</td>
      <td>371159.0</td>
      <td>373159.0</td>
      <td>373330.0</td>
      <td>376633.0</td>
      <td>378300.0</td>
      <td>381633.0</td>
      <td>388000.0</td>
      <td>394667.0</td>
      <td>407333.0</td>
      <td>419330.0</td>
      <td>432663.0</td>
      <td>438297.0</td>
      <td>434967.0</td>
      <td>428300.0</td>
      <td>419000.0</td>
      <td>410667.0</td>
      <td>403667.0</td>
      <td>398000.0</td>
      <td>396667.0</td>
      <td>400150.0</td>
      <td>411813.0</td>
      <td>426480.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Select list price index from February 2022</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[11]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">home_prices</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">home_prices</span><span class="o">.</span><span class="n">index</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">home_prices</span> <span class="o">=</span> <span class="n">home_prices</span><span class="p">[[</span><span class="s1">&#39;RegionName&#39;</span><span class="p">,</span> <span class="s1">&#39;StateName&#39;</span><span class="p">,</span> <span class="s1">&#39;2021-02-28&#39;</span><span class="p">]]</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Take City from RegionName</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[12]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">home_prices</span><span class="p">[</span><span class="s1">&#39;city&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">home_prices</span><span class="p">[</span><span class="s1">&#39;RegionName&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39;,&#39;</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">home_prices</span><span class="o">.</span><span class="n">drop</span><span class="p">([</span><span class="s1">&#39;RegionName&#39;</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">home_prices</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">{</span><span class="s1">&#39;2021-02-28&#39;</span><span class="p">:</span> <span class="s1">&#39;list_price&#39;</span><span class="p">},</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">home_prices</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[12]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>StateName</th>
      <th>list_price</th>
      <th>city</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>CA</td>
      <td>849296.0</td>
      <td>Los Angeles</td>
    </tr>
    <tr>
      <th>3</th>
      <td>IL</td>
      <td>299900.0</td>
      <td>Chicago</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TX</td>
      <td>330293.0</td>
      <td>Dallas</td>
    </tr>
    <tr>
      <th>5</th>
      <td>TX</td>
      <td>315999.0</td>
      <td>Houston</td>
    </tr>
    <tr>
      <th>6</th>
      <td>VA</td>
      <td>436967.0</td>
      <td>Washington</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Create buckets of list price range for the cities in the analysis</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[13]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">home_prices</span><span class="p">[</span><span class="s1">&#39;list_price_range&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">qcut</span><span class="p">(</span><span class="n">home_prices</span><span class="p">[</span><span class="s1">&#39;list_price&#39;</span><span class="p">],</span> <span class="n">q</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">labels</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;low&#39;</span><span class="p">,</span> <span class="s1">&#39;mid_low&#39;</span><span class="p">,</span> <span class="s1">&#39;mid&#39;</span><span class="p">,</span> <span class="s1">&#39;mid_high&#39;</span><span class="p">,</span> <span class="s1">&#39;high&#39;</span><span class="p">])</span>
<span class="n">home_prices</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[13]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>StateName</th>
      <th>list_price</th>
      <th>city</th>
      <th>list_price_range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>CA</td>
      <td>849296.0</td>
      <td>Los Angeles</td>
      <td>high</td>
    </tr>
    <tr>
      <th>3</th>
      <td>IL</td>
      <td>299900.0</td>
      <td>Chicago</td>
      <td>mid_high</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TX</td>
      <td>330293.0</td>
      <td>Dallas</td>
      <td>high</td>
    </tr>
    <tr>
      <th>5</th>
      <td>TX</td>
      <td>315999.0</td>
      <td>Houston</td>
      <td>high</td>
    </tr>
    <tr>
      <th>6</th>
      <td>VA</td>
      <td>436967.0</td>
      <td>Washington</td>
      <td>high</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[14]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">home_prices</span><span class="p">[</span><span class="s1">&#39;city&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[14]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>826</pre>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[15]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">home_prices</span><span class="p">[</span><span class="s1">&#39;StateName&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[15]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>50</pre>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Subset to only States</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[17]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">us_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;territory_abbr.csv&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[18]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">us_data</span><span class="o">.</span><span class="n">columns</span> <span class="o">=</span> <span class="n">us_data</span><span class="o">.</span><span class="n">columns</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<span class="n">us_data</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;state&#39;</span><span class="p">:</span> <span class="s1">&#39;longform&#39;</span><span class="p">,</span> <span class="s1">&#39;abbreviation&#39;</span><span class="p">:</span> <span class="s1">&#39;state&#39;</span><span class="p">},</span> <span class="n">inplace</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">us_data</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[18]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>longform</th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alabama</td>
      <td>AL</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Alaska</td>
      <td>AK</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Arizona</td>
      <td>AZ</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arkansas</td>
      <td>AR</td>
    </tr>
    <tr>
      <th>4</th>
      <td>California</td>
      <td>CA</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[19]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span> <span class="o">=</span> <span class="n">business_data</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">us_data</span><span class="p">,</span> <span class="n">how</span> <span class="o">=</span> <span class="s1">&#39;inner&#39;</span><span class="p">,</span> <span class="n">on</span> <span class="o">=</span> <span class="s1">&#39;state&#39;</span><span class="p">)</span>
<span class="n">business_data</span><span class="p">[</span><span class="s1">&#39;state&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">nunique</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[19]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>27</pre>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Merge-business-data-with-home-price-data">Merge business data with home price data<a class="anchor-link" href="#Merge-business-data-with-home-price-data">&#182;</a></h3>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[20]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span> <span class="o">=</span> <span class="n">business_data</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">home_prices</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s1">&#39;inner&#39;</span><span class="p">,</span> <span class="n">on</span><span class="o">=</span><span class="s1">&#39;city&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Rank cities by list price</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[21]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span><span class="p">[</span><span class="s1">&#39;list_price&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">isna</span><span class="p">()</span><span class="o">.</span><span class="n">sum</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[21]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>3508</pre>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[22]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span> <span class="o">=</span> <span class="n">business_data</span><span class="p">[</span><span class="n">business_data</span><span class="p">[</span><span class="s1">&#39;list_price&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">notna</span><span class="p">()]</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[26]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">business_data</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">&#39;list_price&#39;</span><span class="p">,</span> <span class="n">ascending</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[26]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>attributes_happyhour</th>
      <th>business_id</th>
      <th>categories</th>
      <th>city</th>
      <th>is_open</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>name</th>
      <th>neighborhood</th>
      <th>postal_code</th>
      <th>review_count</th>
      <th>stars</th>
      <th>state</th>
      <th>longform</th>
      <th>StateName</th>
      <th>list_price</th>
      <th>list_price_range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>89875</th>
      <td>1910 Donner St</td>
      <td>NaN</td>
      <td>vRR8UF2omrnJCytRm2163w</td>
      <td>Guest Houses, Hotels &amp; Travel, Active Life, Bi...</td>
      <td>Boston</td>
      <td>1</td>
      <td>40.310398</td>
      <td>-79.827071</td>
      <td>Trailside Treasures</td>
      <td>NaN</td>
      <td>15135</td>
      <td>3</td>
      <td>4.5</td>
      <td>PA</td>
      <td>Pennsylvania</td>
      <td>MA</td>
      <td>598000.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>100725</th>
      <td>43 Village Way</td>
      <td>NaN</td>
      <td>fafUy1LiEwQk41L1cwN1Jg</td>
      <td>Shopping Centers, Shopping</td>
      <td>Hudson</td>
      <td>1</td>
      <td>41.242013</td>
      <td>-81.442258</td>
      <td>First &amp; Main Hudson</td>
      <td>NaN</td>
      <td>44236</td>
      <td>3</td>
      <td>4.0</td>
      <td>OH</td>
      <td>Ohio</td>
      <td>NY</td>
      <td>499666.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>100772</th>
      <td>76 Maple Dr</td>
      <td>NaN</td>
      <td>3Cnonn4ook40H8Pu1NeDMw</td>
      <td>Jewelry, Shopping, Antiques</td>
      <td>Hudson</td>
      <td>1</td>
      <td>41.238861</td>
      <td>-81.436291</td>
      <td>Cambridge Jewelers</td>
      <td>NaN</td>
      <td>44236</td>
      <td>4</td>
      <td>5.0</td>
      <td>OH</td>
      <td>Ohio</td>
      <td>NY</td>
      <td>499666.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>100770</th>
      <td>87 1st St</td>
      <td>NaN</td>
      <td>q1fTFstlN3AbkCFKRWeeGQ</td>
      <td>Shopping, Plus Size Fashion, Men's Clothing, F...</td>
      <td>Hudson</td>
      <td>1</td>
      <td>41.241614</td>
      <td>-81.441681</td>
      <td>Jos. A. Bank</td>
      <td>NaN</td>
      <td>44236</td>
      <td>3</td>
      <td>3.0</td>
      <td>OH</td>
      <td>Ohio</td>
      <td>NY</td>
      <td>499666.0</td>
      <td>high</td>
    </tr>
    <tr>
      <th>100769</th>
      <td>180 West Streetsboro St</td>
      <td>True</td>
      <td>8yb5gF97PCDE5zbK19Iwpg</td>
      <td>Restaurants, Karaoke, Nightlife, Japanese, Bars</td>
      <td>Hudson</td>
      <td>1</td>
      <td>41.238537</td>
      <td>-81.449617</td>
      <td>Otani Steakhouse and Sushi</td>
      <td>NaN</td>
      <td>44236</td>
      <td>58</td>
      <td>4.0</td>
      <td>OH</td>
      <td>Ohio</td>
      <td>NY</td>
      <td>499666.0</td>
      <td>high</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h3 id="Use-only-food-establishments">Use only food establishments<a class="anchor-link" href="#Use-only-food-establishments">&#182;</a></h3>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[27]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">food_establishments</span> <span class="o">=</span> <span class="n">business_data</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
<span class="n">food_establishments</span><span class="p">[</span><span class="s1">&#39;categories&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">food_establishments</span><span class="p">[</span><span class="s1">&#39;categories&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span>
<span class="n">filt_food</span> <span class="o">=</span> <span class="n">food_establishments</span><span class="p">[</span><span class="s1">&#39;categories&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="n">pat</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">&#39;dining|restaurant&#39;</span><span class="p">,</span> <span class="n">regex</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">==</span> <span class="kc">True</span>
<span class="n">food_establishments</span> <span class="o">=</span> <span class="n">food_establishments</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">filt_food</span><span class="p">]</span>
<span class="n">food_establishments</span><span class="p">[</span><span class="s1">&#39;categories&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[27]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>28638</pre>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[28]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">food_establishments</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[28]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>attributes_happyhour</th>
      <th>business_id</th>
      <th>categories</th>
      <th>city</th>
      <th>is_open</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>name</th>
      <th>neighborhood</th>
      <th>postal_code</th>
      <th>review_count</th>
      <th>stars</th>
      <th>state</th>
      <th>longform</th>
      <th>StateName</th>
      <th>list_price</th>
      <th>list_price_range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>AjEbIBw6ZFfln7ePHha9PA</td>
      <td>chicken wings, burgers, caterers, street vendo...</td>
      <td>Henderson</td>
      <td>0</td>
      <td>35.960734</td>
      <td>-114.939821</td>
      <td>CK'S BBQ &amp; Catering</td>
      <td>NaN</td>
      <td>89002</td>
      <td>3</td>
      <td>4.5</td>
      <td>NV</td>
      <td>Nevada</td>
      <td>NC</td>
      <td>162800.0</td>
      <td>mid_low</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2850 Bicentennial Pkwy</td>
      <td>NaN</td>
      <td>V2td86VD0ezfCJcmUz-ddQ</td>
      <td>sandwiches, salad, restaurants, food, juice ba...</td>
      <td>Henderson</td>
      <td>1</td>
      <td>35.942966</td>
      <td>-115.115893</td>
      <td>Tropical Smoothie Cafe</td>
      <td>NaN</td>
      <td>89044</td>
      <td>52</td>
      <td>1.5</td>
      <td>NV</td>
      <td>Nevada</td>
      <td>NC</td>
      <td>162800.0</td>
      <td>mid_low</td>
    </tr>
    <tr>
      <th>9</th>
      <td>12300 Las Vegas Blvd S</td>
      <td>NaN</td>
      <td>V90fC_aF-_DNYzQvUtbLww</td>
      <td>hotels &amp; travel, asian fusion, day spas, casin...</td>
      <td>Henderson</td>
      <td>1</td>
      <td>35.965173</td>
      <td>-115.168773</td>
      <td>Jayde Fuzion</td>
      <td>NaN</td>
      <td>89044</td>
      <td>246</td>
      <td>3.5</td>
      <td>NV</td>
      <td>Nevada</td>
      <td>NC</td>
      <td>162800.0</td>
      <td>mid_low</td>
    </tr>
    <tr>
      <th>15</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>yZ5yE5HV-BCAfI0pEi22eA</td>
      <td>food stands, food, restaurants, street vendors</td>
      <td>Henderson</td>
      <td>0</td>
      <td>35.960734</td>
      <td>-114.939821</td>
      <td>Foodslingers</td>
      <td>NaN</td>
      <td>89002</td>
      <td>5</td>
      <td>4.5</td>
      <td>NV</td>
      <td>Nevada</td>
      <td>NC</td>
      <td>162800.0</td>
      <td>mid_low</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2980 St Rose Pkwy, Ste 120</td>
      <td>NaN</td>
      <td>UwXOqtr0LCoWsGXP96fOuQ</td>
      <td>food, fast food, filipino, ethnic food, restau...</td>
      <td>Henderson</td>
      <td>1</td>
      <td>36.005404</td>
      <td>-115.117832</td>
      <td>Fiesta Filipina Cuisine</td>
      <td>Anthem</td>
      <td>89183</td>
      <td>172</td>
      <td>3.5</td>
      <td>NV</td>
      <td>Nevada</td>
      <td>NC</td>
      <td>162800.0</td>
      <td>mid_low</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h1 id="Data-Analysis">Data Analysis<a class="anchor-link" href="#Data-Analysis">&#182;</a></h1>
</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Are-higher-rated-restaurants-the-most-reviewd?">Are higher rated restaurants the most reviewd?<a class="anchor-link" href="#Are-higher-rated-restaurants-the-most-reviewd?">&#182;</a></h2>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[30]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_yscale</span><span class="p">(</span><span class="s1">&#39;log&#39;</span><span class="p">)</span>

<span class="n">sns</span><span class="o">.</span><span class="n">boxplot</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">food_establishments</span><span class="p">,</span> <span class="n">x</span> <span class="o">=</span> <span class="s1">&#39;stars&#39;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="s1">&#39;review_count&#39;</span><span class="p">,</span> <span class="n">notch</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">suptitle</span><span class="p">(</span><span class="s1">&#39;Relationship between Stars and No. of Reviews&#39;</span><span class="p">,</span> <span class="n">fontsize</span> <span class="o">=</span> <span class="mi">25</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;Number of reviews&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[30]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>Text(0, 0.5, &#39;Number of reviews&#39;)</pre>
</div>

</div>

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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1UCr1UKhUOjbgiAYtC2Vg4MDvvzySzRp0gRqtRrPPfccDh8+LHZZ1ebGjRt47rnnMGfOHPj6+up/bun729h2W/r+njVrFk6cOIH4+Hhs3rxZ/3NL39/GtttS9/eWLVvg6emJ4ODgUh+31P1d3nZb6v5u164dPvroIzg5OcHFxQVjxowx2C4p7m8Gs2pQr149JCUl6dv37983eurPksTFxWHr1q36tiAIUKvVIlZUfc6ePYspU6bgtddew8iRIw0es+T9XdZ2W+r+joyMRHh4OADAzs4OAwYMwPXr1/WPW+r+Lm+7LXV///777zh27BiGDx+OVatW4cCBA1i8eLH+cUvd3+Vtt6Xu7zNnzuDEiRP6dvHtkuL+ZjCrBl5eXrCxscHZs2cBADt37kSPHj1Ersr0bG1tsWzZMty9exeCIGDjxo3o37+/2GU9svj4eEyfPh3Lly/HkCFDSjxuqfu7vO221P0dExODhQsXIi8vD3l5edi/fz86dOigf9xS93d5222p+/vbb7/F7t27sXPnTsyaNQt9+vTB/Pnz9Y9b6v4ub7stdX8/fPgQH330EXJzc5GRkYEdO3YYbJcU9zeD2SN44YUX8M8//wAAli9fjiVLluDxxx9HVlYWJk2aJHJ1pqPbbhcXF7z33nuYNm0aHn/8cQiCgGeffVbs8h7Z119/jdzcXHz44Yf626t/+ukni9/f5W23pe7vnj17olevXhgxYgRGjx6Ndu3aYciQIRa/v8vbbkvd38ZY+v42xtL3d+/evdGzZ0/937nub13K+1shCIIgagVEREREBIA9ZkRERESSwWBGREREJBEMZkREREQSwWBGREREJBEMZkREREQSwWBGRLL23HPPISUlRewyiIgAMJgRkcwVnTePiEhsNX++BSKiCsjMzMS8efMQHR0NpVKJwMBAFBQUAAAmT56ML774AteuXcO6deuQl5eHlJQUjBgxArNnz8apU6ewaNEi2NvbIzMzEz/++CMWLFhg8FrvvfcelEp+1yWiR8OjCBHJwp9//onMzEzs3LlTPydgSEgIAGDDhg2oV68evvnmG3z44YfYvn07Nm3ahC+++EJ/mvPGjRtYsWIFdu3ahf3795d4rbt374qzYURkUdhjRkSy0KFDB6xcuRITJ05Ely5dMHnyZPj4+OgfVygUCA0NxaFDh7B7925ERkZCEARkZ2cDADw9PeHl5VWh1yIiqir2mBGRLDRo0AB//vknpk6dioyMDDz77LM4cOCA/vGsrCyMHDkSV65cQYsWLTBnzhyo1WroZq2zt7ev8GsREVUVe8yISBZ+/PFHnD17FsuXL0f37t2RnJyMq1evQqVSQaPRIDo6GhkZGZg9ezasra3xyy+/IC8vD1qttsKv1adPHxG2jIgsCYMZEcnCiBEjcPr0aQwePBh2dnbw9PTExIkTcevWLUycOBGffvopevXqhUGDBsHa2hp+fn5o2rQpoqOjYW1tXaHXIiJ6VApB109PRERERKLiNWZEREREEsFgRkRERCQRDGZEREREEsFgRkRERCQRDGZEREREEsFgRkRERCQRDGZEREREEsFgRkRERCQR/w+171RwKVSg6QAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Do-food-establishments-in-cities-with-higher-listing-prices-have-higher-ratings?">Do food establishments in cities with higher listing prices have higher ratings?<a class="anchor-link" href="#Do-food-establishments-in-cities-with-higher-listing-prices-have-higher-ratings?">&#182;</a></h2>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[33]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">food_establishments</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;list_price_range&#39;</span><span class="p">])[</span><span class="s1">&#39;stars&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">agg</span><span class="p">([</span><span class="s1">&#39;count&#39;</span><span class="p">,</span> <span class="s1">&#39;mean&#39;</span><span class="p">,</span> <span class="s1">&#39;median&#39;</span><span class="p">,</span> <span class="s1">&#39;std&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">round</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[33]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>median</th>
      <th>std</th>
    </tr>
    <tr>
      <th>list_price_range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>low</th>
      <td>361</td>
      <td>3.30</td>
      <td>3.5</td>
      <td>0.84</td>
    </tr>
    <tr>
      <th>mid_low</th>
      <td>3839</td>
      <td>3.46</td>
      <td>3.5</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>mid</th>
      <td>2707</td>
      <td>3.51</td>
      <td>3.5</td>
      <td>0.80</td>
    </tr>
    <tr>
      <th>mid_high</th>
      <td>7870</td>
      <td>3.47</td>
      <td>3.5</td>
      <td>0.82</td>
    </tr>
    <tr>
      <th>high</th>
      <td>13861</td>
      <td>3.46</td>
      <td>3.5</td>
      <td>0.81</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Is-Mexican-food-better-rated-in-border-states-than-the-rest-of-the-US?">Is Mexican food better rated in border states than the rest of the US?<a class="anchor-link" href="#Is-Mexican-food-better-rated-in-border-states-than-the-rest-of-the-US?">&#182;</a></h2>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[34]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">filt_mexican</span> <span class="o">=</span> <span class="n">food_establishments</span><span class="p">[</span><span class="s1">&#39;categories&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="n">pat</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">&#39;mexican&#39;</span><span class="p">,</span> <span class="n">regex</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span> <span class="o">==</span> <span class="kc">True</span>
<span class="n">mexican_establishments</span> <span class="o">=</span> <span class="n">food_establishments</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">filt_mexican</span><span class="p">]</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[35]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">len</span><span class="p">(</span><span class="n">mexican_establishments</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[35]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>3261</pre>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[36]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">border_state</span> <span class="o">=</span> <span class="p">[</span><span class="s1">&#39;CA&#39;</span><span class="p">,</span> <span class="s1">&#39;AZ&#39;</span><span class="p">,</span> <span class="s1">&#39;NM&#39;</span><span class="p">,</span> <span class="s1">&#39;TX&#39;</span><span class="p">]</span>
<span class="n">mexican_establishments</span><span class="p">[</span><span class="s1">&#39;border&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">mexican_establishments</span><span class="p">[</span><span class="s1">&#39;state&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">isin</span><span class="p">(</span><span class="n">border_state</span><span class="p">)</span> <span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
<span class="n">mexican_establishments</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="application/vnd.jupyter.stderr">
<pre>/opt/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:2: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame.
Try using .loc[row_indexer,col_indexer] = value instead

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  
</pre>
</div>
</div>

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[36]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>address</th>
      <th>attributes_happyhour</th>
      <th>business_id</th>
      <th>categories</th>
      <th>city</th>
      <th>is_open</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>name</th>
      <th>neighborhood</th>
      <th>postal_code</th>
      <th>review_count</th>
      <th>stars</th>
      <th>state</th>
      <th>longform</th>
      <th>StateName</th>
      <th>list_price</th>
      <th>list_price_range</th>
      <th>border</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70462</th>
      <td>3800 E Sky Harbor Blvd</td>
      <td>True</td>
      <td>JDwUNHYA_-FvxEMRvHniig</td>
      <td>mexican, nightlife, bars, american (traditiona...</td>
      <td>Phoenix</td>
      <td>1</td>
      <td>33.435148</td>
      <td>-111.998369</td>
      <td>Taberna del Tequila</td>
      <td>NaN</td>
      <td>85034</td>
      <td>59</td>
      <td>2.0</td>
      <td>AZ</td>
      <td>Arizona</td>
      <td>AZ</td>
      <td>379600.0</td>
      <td>high</td>
      <td>1</td>
    </tr>
    <tr>
      <th>74842</th>
      <td>5632 N 7th St</td>
      <td>NaN</td>
      <td>c0F2t2j9MJ2gUBUPky-dqw</td>
      <td>restaurants, mexican</td>
      <td>Phoenix</td>
      <td>0</td>
      <td>33.519553</td>
      <td>-112.065159</td>
      <td>Barrio Urbano</td>
      <td>NaN</td>
      <td>85014</td>
      <td>178</td>
      <td>3.5</td>
      <td>AZ</td>
      <td>Arizona</td>
      <td>AZ</td>
      <td>379600.0</td>
      <td>high</td>
      <td>1</td>
    </tr>
    <tr>
      <th>103353</th>
      <td>607 N Cunningham Ave</td>
      <td>NaN</td>
      <td>BsxefnHbrpDN7HB2hJrEiw</td>
      <td>food, mexican, street vendors, restaurants</td>
      <td>Urbana</td>
      <td>1</td>
      <td>40.118616</td>
      <td>-88.204113</td>
      <td>Taco Motorizado</td>
      <td>NaN</td>
      <td>61802</td>
      <td>37</td>
      <td>4.5</td>
      <td>IL</td>
      <td>Illinois</td>
      <td>OH</td>
      <td>183767.0</td>
      <td>mid</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15792</th>
      <td>8431 Farm Rd, Ste 110</td>
      <td>NaN</td>
      <td>5WOE18ldtQ1U0MK5fN2HGQ</td>
      <td>seafood, mexican, salad, restaurants</td>
      <td>Las Vegas</td>
      <td>1</td>
      <td>36.299397</td>
      <td>-115.281123</td>
      <td>Rubio's Coastal Grill</td>
      <td>Centennial</td>
      <td>89143</td>
      <td>46</td>
      <td>4.0</td>
      <td>NV</td>
      <td>Nevada</td>
      <td>NM</td>
      <td>235900.0</td>
      <td>mid_high</td>
      <td>0</td>
    </tr>
    <tr>
      <th>119796</th>
      <td>Nc Hwy 74 At Wellness Blvd</td>
      <td>NaN</td>
      <td>uMesmY4M3Nx6I4WLI1p1IQ</td>
      <td>tex-mex, restaurants, mexican, american (tradi...</td>
      <td>Monroe</td>
      <td>1</td>
      <td>35.023305</td>
      <td>-80.579382</td>
      <td>Moe's Southwest Grill</td>
      <td>NaN</td>
      <td>28110</td>
      <td>9</td>
      <td>2.5</td>
      <td>NC</td>
      <td>North Carolina</td>
      <td>LA</td>
      <td>209983.0</td>
      <td>mid</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[37]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mexican_establishments</span><span class="p">[</span><span class="s1">&#39;border&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[37]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>0    2489
1     772
Name: border, dtype: int64</pre>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[38]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">))</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_yscale</span><span class="p">(</span><span class="s1">&#39;log&#39;</span><span class="p">)</span>

<span class="n">sns</span><span class="o">.</span><span class="n">boxplot</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">mexican_establishments</span><span class="p">,</span> <span class="n">x</span> <span class="o">=</span> <span class="s1">&#39;border&#39;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="s1">&#39;review_count&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">suptitle</span><span class="p">(</span><span class="s1">&#39;Relationship between Review Count and Border State&#39;</span><span class="p">,</span> <span class="n">fontsize</span> <span class="o">=</span> <span class="mi">25</span><span class="p">)</span>
<span class="n">ax</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">&#39;Number of reviews&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[38]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>Text(0, 0.5, &#39;Number of reviews&#39;)</pre>
</div>

</div>

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,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unfvrk2bNmX43HPnzunBBx/U7NmzdfHiRYWFhenixYv69ddfNWjQIP32228uj9+2bZv69OmjZcuWKTY2VrVr11bFihW1b98+zZkzR71799Y///yT4bLef/99Pf7449qxY4eqV6+u4sWLa9++fXr77bc1bNiwHO3ZJyYmqn///vrss8/k7++vunXr6sSJE5o/f77uvfdeM/jmxKlTp9SnTx8tXbpUJUqUUO3atRUVFaU5c+aoV69eLj8Up0WLFunee+/VN998o7Nnz6pevXoKDg5WZGSkRo8ereeee06pqanm4xs1aiS73W62nX/j4sWLq06dOpKunhd5rfXr10u6+r269r3FxMRo9+7dCgwMVLt27czbp06dqoceekg//vijkpKSZLfb5efnp1WrVmnIkCF666230i0nJSVFzz//vEaOHKnVq1fLZrOpfv36SkpK0rfffqv7778/00Np77zzjkaNGqW//vpL1apVU/HixbV7925NnjxZL7zwgtvn5dXq1at14cIFSVcPr6Z14cIFPfbYYxo7dqw2bdqkYsWKyW63KyEhQYsXL1bPnj31008/mY+/5ZZbVL16daWkpOi7777LcHmrVq1SYmKiqlatqtatW2daW06Xf/vtt0uStmzZosuXL7u81rZt23Tx4kVJ0saNG9Mty/l77dChQ5bnrKV9rfDw8Ewf6xQWFqYuXbqofPnyLrcnJiZqwIABGj9+vDZv3qySJUuqfv36On/+vFauXKk+ffpo/vz52VpGdiUnJ2vo0KGaMmWKYmNjVbduXaWmpmrjxo0aOXKky7lflStXVvPmzc0dxZo1a6p58+bZHtw2bdo0DRw4UCtXrtSFCxdUp04dValSRadPn9ZPP/2kIUOG6KuvvsrwuSdOnFCvXr3M303dunV15swZ/ec//9GDDz6oXbt2pXvOq6++qlGjRmnjxo0KCgpS7dq1tXPnTj366KNavnx5Tj+qbPv5558lXf18rh3pnZycrFGjRmn06NFau3atAgIC1KBBA6WkpJifgfO0how8+eST+vbbb1W9enUFBQWpQoUK5nc0t+83p+vftObMmaOZM2eqePHiqlSpkhITE112pjISHBxsbpPfffddjRkzRr///nuGy6hQoYLCwsJUpkwZ8za73a5GjRqZ7YYNG6p58+bmKVKXL182d85+/fVXFSlSRHa7XaVLl1ZUVJS++uor3Xvvvfr777/N13C3TUnbq56bbUGGjAJit9sNu91uLF261O1jrly5YixcuNC44YYbDLvdbowbN87l/gsXLhidOnUy7Ha7MWLECOPkyZPmfbGxscawYcMMu91udO7c2bh06ZJ539KlSw273W7ceuutLq83ZswYw263G506dTIOHz7sct+aNWuMm266ybDb7cYbb7zhcp+71zMMw+jYsaNht9uNxYsXm7edP3/eaNeunWG3240HH3zQOHr0qHlfXFycMXz4cMNutxstWrRwuc+5HLvdboSHhxtr164174uJiTF69Ohh2O1245577nGp4f777zfsdrsxceJE48qVK+btR48eNTp37mzY7Xbj5ZdfdnmOcznO93vhwgXDMAzD4XAYc+bMMe/77bffMnzeunXrMqy7UaNGRkREhHnfyZMnjQcffNCw2+3G3XffbSQnJ6f7DDMyc+ZM8zVbt25t/P777+Z9hw4dMrp27WrY7Xajf//+Ls9bvXq1Ub9+faNhw4bGwoULjZSUFPO+9evXG23atDHsdrsxffp0l+dt3LjRXF7aGt98803DbrcbzzzzjMvjDx065PIZzp8/3+X+r776yrDb7cawYcPM27744gvDbrcbN998s7FixQrzdofDYXz33XdG06ZN032XDMMwpk6datjtdqN9+/bGmjVrzNtTUlKMTz75xLjxxhuN+vXrG5GRkS7PS1vftGnTjMuXL5vPc76m3W43/v7773SfvzsPPfSQYbfbjTFjxrh9TGpqqrF69Wrzs+7atauRlJTk8phnnnnG/E7s2LHDvP3y5cvG22+/bdjtdqNx48bG3r17zfvee+89w263G/fff3+Gyx06dKhht9uNd955x7zN+Zt/7rnn8rR8h8NhhIeHG3a73eVvYBiGMW3aNPOzbNCggXHmzBmX+53f/++//97tZ+a0aNEi87X++eefLB+fGed6Jjw83Ni4caN5+5UrV4x33nnHXM6PP/5o3hcdHW3eHhUVleHrOtd5adftaX8/TZs2NVauXGned+7cOWPw4MGG3W43brnllnTrgIzWoVlxLq9BgwbG119/baSmppr3/fPPP+b3tG3bti73pV2vdOnSxdi5c6d538GDB4327dub25u0VqxYYdjtdqNhw4Yu7+3s2bPG6NGjzdfMaBvhTtr15rWuXLlinDx50vjiiy+Mpk2bGg0aNEj3vTMMw5gwYYL5maf9fqWkpBifffaZceONN2a4fkq7vt68ebNhGFd/t87vbm7fb27Xv86/l91uN+bNm2feHh8fn/mH+H927dplrj+d/zVv3twYOnSoMXfuXGP79u0u34NrZfa9d35nWrVq5bKuMAzD2LFjh7leePLJJ13uc7dNMYzcbwsyUuA9cXPnzlW/fv1c/uvbt6+6d++uFi1aaNKkSUpNTVW3bt3MEzidlixZoiNHjqhhw4Z69913XQ5nVahQQTNmzFDVqlUVFRWlZcuWZVpHSkqKtmzZIpvNphdffDFdur/11lvVrVs3SXk/f+fzzz9XbGysypcvr7lz56p69ermfeXLl9fMmTNlt9t1/vx584TMa/373/926cEJDQ3VqFGjJF3tqnb2cDjbknTfffe5HP6sXr26xowZo44dO6pq1aoZLic8PFxjxowxz12y2WwaNmyYucf3xx9/5Oi9jxkzRt27dzfbFStW1Pvvv6+SJUtq//79+vHHH3P0etLVPZa0h5Br166t9957T/7+/tqyZYu2bNli3vf222/LMAw9//zzGjRokMsJrm3atNHkyZMlXT0cfObMmSyX7eyBWbdunUuvpLMXznm+yrW9qr/++qskmYePkpKS9O6770qSXn/9dd1zzz3mY202m7p166Z//etfkq7uTToPocTHx5sjtt9//33deuut5vP8/f01cOBADRkyRIZh6J133snwPXTs2FHPPvusuRfo7++vp59+WqVLl5Ykbd26NcvP4Vpr1qxJ97vu16+fevbsqdatW2vo0KGKj49XgwYNNG/ePJdDtnv27NF3332noKAgffTRRy6970WLFtUzzzyjrl276sqVKy4jxnr37i0/Pz/t2LFDR44ccaknPj5e69atk81mczsaPi/Lt9lsuu222ySl75Vdt26dJOnmm2+Ww+HQ77//bt535swZ7dixQ4GBgS5/O3fOnj1r/js7h1Ld2b59u/kdnDlzpstccoGBgXrqqaf04IMPSlK+z583evRo9ejRw2yXLFnS/G4nJCTky3lda9euVWBgoDp16qT77rvP5TBypUqV9NRTT0m62pMfHx+f4WtMmzZNjRs3Ntt16tTRkCFDJKX/TcyePVuS9Pjjj7u8t1KlSumtt97K81yI9evXd/mvcePGat++vV555RUlJSVp1qxZ6b4/J0+e1JdffilJmjhxou666y7zPn9/fw0YMMD8HN577z2XbYZT165dzXWYn5+fQkJC8vR+87r+rVq1qh577DGznd3fwI033qglS5aoRYsW5m2JiYlavXq1pk2bpgceeEDt2rXT9OnTdenSpWy9ptP69evl5+enUaNGpTtS2KRJE/Xr109S9nNDbrcF7hR4iIuKitLWrVtd/tu2bZv279+vKlWqaODAgfryyy81ffr0dJPwObuRu3Xrlm60iXR1hJbz+LpzheVOQECAfv75Z+3YscNcGadlGIYZZK49XJJTv/zyiySpV69e5oYyrcDAQA0cONB8rHHNeYD+/v5q3759uuelPS8g7Sgl53krr7zyijZs2KDk5GTzvttvv11z5sxxex6D8/h/WjabzewKPn36dMZvMgPBwcEZzvNUtmxZderUSdLVQ145UatWrQwPK9WpU8cMds65+44dO6bdu3dLkssPI60OHTqoTJkyunz5sjZs2JDl8ps1a6ayZcsqISHB5RCLc8P9xBNPyGazuXTfJyUlaePGjfLz8zMH7TjP2SlevLh5ztG17rnnHvn5+SkmJsbsml+9erWSkpIUFhaW4XlvktSzZ09JV899y2iD5Qyiafn7+5vfm3PnzmX5OVwrPj4+3e9669at2rNnj2w2m3r27KmZM2dq2bJl6SZw/e9//yvp6iHSjKbtSfue1qxZY36uVapUMQ+TRkREuDw+IiJCKSkpatmypctOU0Zyu/y0gd4pISFBf//9t+x2u/kdT3tIdc2aNXI4HGrTpo3b85nSSjvqO+3vOKec68MmTZq4Pf3jkUcekSQdOXIkXweepB2o5pR23ZWb79u1nn/+ee3cudPtIae025KM1uehoaEZ/p6cp0+cP3/evC06OlqHDh2SdHVH4lqBgYHq06dPzt7ANZyH25z/NWnSRDVr1pSfn59SUlI0duxYLVmyxOU5a9asUUpKiipUqGB2QFzroYceUpEiRXT+/PkMJ+lOG3qccvt+82P926xZs1xPihsWFqbPP/9c33zzjUaNGqVmzZq57DzGx8drzpw5uueee1xOmcrKF198oZ07d6pv374Z3u/8zWY3N+R2W+BOgQ9sSHvyq8Ph0PHjx/Xhhx/qyy+/VGxsrGrVqqVmzZpl+FznimXJkiVuN/6nTp2SJPNLl5WiRYsqPj5e27dvV1RUlI4dO6ZDhw5p9+7d5l5wXkd4Ofc03W100953+vRpJSQkuByjL126dIazSqc9np42nf/rX//SiBEjtGPHDg0ZMkTBwcFq2bKl2rZtq9tuuy3TcwrcbcRyE2jr16/vdiSd80TaqKiobL+elPlnWL9+fW3atMk8J3L//v3mfSNHjnT7vCtXrkjK3nfGz89Pt912m5YtW6Z169apcePGSklJ0aZNmxQSEqLWrVsrLCxM+/fv165du9SkSRNt3LhRFy9eVLNmzczzlJy1JScna8CAAW6X5+/vL4fDoUOHDqlJkybm806ePGnu8V0r7U7AoUOH0g1icfc3dn7H3J2fkpnevXub88QZhqGzZ89q+fLleuedd3T27FkFBgaqY8eOGe58Od/TX3/95fY9Of9GFy5cUExMjDkv4X333af169crIiLC7JmWZA4GyGijk1/Lb9u2rYKCgrR//37FxMSoYsWKWr9+vRnSnBvEtCHOeT5c2hP6M5N2sNOZM2eyFfwy4vxuZ/b7qVWrlkqUKKHExEQdPnzY5RyevMjo+5Z2fZab71tGbDab/Pz8tGXLFh04cEDR0dE6evSo9u7d69JTm9H6PKvfRNr1q/OzLF68uNsjGjfccEOu34fkfp64hIQEzZgxQ59//rnGjx+v4sWLm4HNWdcNN9yQbkCLU3BwsGrXrq19+/bp8OHD6QJ2RoPNcvt+82P9m9vBb9fWdsMNN+jJJ5/UpUuXtHXrVkVGRmrFihWKj4/X0aNH9dRTT7k9XzIjziC8detWRUVFKTo6WlFRUdq9e7eZQbKbG3K7LXDHo6NT/fz8VL16db366qsqX7683nvvPU2cOFFXrlzRo48+mu7xzt6mqKioLDf+afec3ImLi9OUKVP0ww8/uOzlBgUFqXHjxkpNTc3x4cOMOOvObO64tBOfXrhwwSXEZWe0YNoNd/v27fX111/rgw8+0G+//aYLFy5o9erVWr16tSZPnqwWLVpowoQJCgsLS/c6mU1fkFPOrviMODdGOd0Lz2wj5rzPGTTTfgeyc4gwO98ZSbrjjju0bNkyRUZGmoNAEhMT1aVLF/n5+al169bav3+/Nm7cqCZNmmS44XYuKykpKVu1OT8n5/MSExNz9Ly0svo+XdsTnFM2m00hISF6+OGHVb9+fQ0dOlRLlixRfHy8edg7Led7io+Pd3uoK61z586ZIa5Tp04qVaqUoqKitHPnTjVp0kQHDhzQrl27FBwcnOHIt2vldvnFihVT27ZttWrVKkVGRpqBUrp6qKhhw4YqXbq0Dhw4oFOnTikkJESRkZHy8/PLsDc0I2kPU+3fvz9bl6FyOBzau3ev6tevb27Ms7MOkq7+hhITEzM81JZbBf19c77GwoUL9dFHHyk2Nta83WazqXbt2urZs6dWrFiR6xrTcv6mMrsiRn5dMvJaISEheuWVV3TgwAFt3rxZM2bMMENcdv/Gzm1NRn/jjDoLcvt+82P9m5/bI+nqtj08PFzh4eF66qmn9NJLL+m7777T9u3btWvXrkx3cpycV15Yvny5OehIkjnq+oYbbtDatWuzXVNutwXueG2KkVGjRmn79u2KjIzU1KlTdeONN6YbUhsUFGSeN5ZRF31OXLlyRYMHD9bBgwcVEhKifv36qVGjRqpbt65q1Kghf39/TZ8+PV9CXPHixXX27NlMQ0Lac19yu7ed1g033KC3335bycnJ2rFjhzZt2qT169dr69at+uOPPzRkyBD99NNPBXppnrRf8Gs5P4vMpjrJ6Ws6V2LOFYrzvYWEhLgd+Zsb4eHhKlq0qLZv367ExERzw+08tNe2bVt9+umn2rRpk4YNG2Ye3k3bVe7scm/YsGGW52+m5Xxely5dNHPmzHx5PwWpbdu2GjVqlN555x398ssvmjVrlkaPHu3yGOd7ymg6jqwULVpU3bp105dffqmVK1eqSZMm5sb6rrvuytEhy9ws//bbb9eqVau0bt06M8QFBASoZcuW8vPzU6tWrfTTTz9p06ZNqlChgs6dO+fSI5uVG264QVWrVtXx48e1bt26bK33duzYob59+6p06dKaP3++GjZsaH4OWe2oOO/P6HNzF7Yy+016yqxZs8zzirp166b27dsrLCxMderUUfHixRUVFZVpiMsJ585pZkHX2btUUO644w5t3rxZUVFROn/+vEqWLJntv7EzBGR3O5Pb91tQ69+s/Pvf/9bGjRvVu3dvjRgxwu3jihUrpgkTJuinn34y59zLToh74oknzBHsDz/8sG666SbVq1dPNWvWVJEiRbR48eIchbjcbgvc8doUIzabTa+//rpKliwph8OhMWPGpJuN2rlXmrab9lpRUVH6888/szx36+eff9bBgwcVEBCgr776Sk8//bTuvPNO1a5d2+wpyMlx8sw4z6vIaJi6019//SXp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dccddygsLEw2m02HDx9WUlKSAgIC9Pbbb7u9TIrT7bffrmbNmmnbtm16/fXX9cEHH6hixYqKi4tTTEyMbDab2rZtq/Xr1ys2NlaGYZgrNucJw5cvX9Zdd92l0NBQffTRR24Pg5YqVUpz5szRsGHDtG3bNnXu3FlhYWEKCAjQ/v37lZycrJCQEE2dOjXL2aizY/r06erbt682b96sO++8U9WqVVNQUJCOHTumc+fOyd/fXxMmTMjTvFPZUbJkSRUtWlQDBgxQ7dq1VaxYMe3bt0+pqalq0KCB3nrrrRwPH2/durX27NmjXr16mYdinV35zZs318SJE10ef/fddysqKkrvvvuupk6dqrlz56pWrVo6ffq0uZGoXbu2y/xj0tWNb3BwsC5evKgHHnhA1apV06RJk8yAGBoaqkaNGpkrr2tXQG3btjVfMzQ0NMPRREOHDlV0dLQWL16sl156SW+99ZaqVaummJgY8+Ts5s2b67XXXnN53ksvvaSYmBj9+uuvGjFihEJDQ1WxYkUdP37cPI2gS5cu5grqejFixAh9//33Onz4sGbPnq0uXbqYU0289dZbGj58uHbs2KF+/fqpWrVqKl26tKKjo81zeAYPHux2WH/Pnj01bdo0XbhwQTabLVujUtPKy/Jvv/12TZs2TcnJyQoKCkp3NYrWrVube9g57YVz6tixoz766CONHj1af/75px577DGVKlVK1apVU0pKig4fPmz2bnbv3l2TJk1KFzbffPNNPf7449q2bZsGDRqkqlWrqmzZsjp8+LASExPN+QLvvvtul+c9/fTTGjFihA4cOKA777xTYWFhOnv2rHnouHnz5jmeKigzN954o/bt26cPP/xQa9asUadOnfTEE0+4fXxAQICeeuopvfrqq9q8ebM6dOigWrVqKSkpSUeOHFFKSopuvPFG/fPPPzpz5oxOnjyZrXOfMtOuXTs9//zzmjZtmiZPnqwPPvhAlStX1qFDh3ThwgV16tTJnLomNzIaJX3lyhUdPnzY7HW899570z3uxRdfVExMjFatWqWnnnpKoaGhqlSpkqKjo8152B566CFzhyq7cvt+c7v+zaupU6cqODhY33zzjT755BN98sknqlKlisqVK6crV66YhyWLFCmi5557Tv3793d5fkhIiHku6siRI1WnTh099dRTat++vbp27arvv/9eH3/8sZYvX66qVasqISHBDIrh4eFat26dLly4oMTERHNHOrNtSm63BRnxek+cdDXtPv7445KuHieeNWuWeV/jxo0VERGhkSNHqn79+uaUIOXLl1evXr20dOnSDOc6u5a/v78WLFig559/XjfccIMuXbqkffv2KSAgQN26ddNnn32m999/X0WLFlVCQoLL3nnNmjU1efJk1apVSwkJCfrnn3+y3Gu88cYb9e233+qJJ55QvXr1zCHJtWvX1uOPP66VK1fm+VCqU1hYmJYvX65+/fqpatWqOnHihA4cOKBSpUrpvvvu04oVK1wmbCwowcHBWrJkie6//36dO3dOUVFRCgsL07/+9S998cUXqlSpUo5fs2bNmlqyZInuuusuxcXF6ejRo2rQoIFefPFFLVy4MMO9y5EjR+qrr75Sjx49VKJECe3Zs0dnzpzRjTfeqKeeekpLly5NN8CiePHimjFjhho0aKCLFy/q2LFj6fbm0vauXRvimjZtau553X777RmGVZvNpokTJ+qjjz5Sp06dFBAQoN27d+vChQtq2rSpxo8fr4ULF6YbfFK0aFHNnj1b06dP16233qrk5GTt3r1bqampatWqlXm92ox6rLwpMDBQEydOlM1mU1JSkl5++WWzN6lMmTJatGiRJkyYoFtuuUXnz5/X3r17FRAQoA4dOuj999/XSy+95Pa1y5UrZ86l2Lp1a3P0anblZflhYWHmYaMWLVqku76w85CqlPsQJ8kcJPHCCy+oVatWCgwM1P79+3X06FFVqVJF9957rxYtWqRp06ZlOMowJCREn376qSZOnKiWLVua77FMmTLq06ePvv76a7NHIK327dvr888/15133qng4GAdOHBARYsW1ejRo/X555/n++CoMWPGqEuXLgoKCtKhQ4eydRnF/v37a8GCBQoPDzcnEo+Pj9dNN92kf//731q8eLHZE5nVHKLZNXToUH3yySfmoer9+/erdu3aevvtt81JgnMro7lUDx8+rIoVK6pnz56aP3++Jk+enO7cuMDAQM2aNUvTp09Xu3btlJSUpN27dysoKEh33323PvnkE7388su5mnstt+83N+vfvAoMDNQbb7yhJUuWmNeSTkpK0p49e3Ty5EnVrl1bjz76qFauXJnhd16SZsyYoWbNmsnhcCgqKkpHjx6VdPXUiokTJ6px48bmSPCkpCR17NhRc+fO1ccf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
"
>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[39]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mexican_establishments</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;border&#39;</span><span class="p">])[</span><span class="s1">&#39;stars&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">agg</span><span class="p">([</span><span class="s1">&#39;count&#39;</span><span class="p">,</span> <span class="s1">&#39;mean&#39;</span><span class="p">,</span> <span class="s1">&#39;median&#39;</span><span class="p">,</span> <span class="s1">&#39;std&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">round</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[39]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>median</th>
      <th>std</th>
    </tr>
    <tr>
      <th>border</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2489</td>
      <td>3.48</td>
      <td>3.5</td>
      <td>0.79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>772</td>
      <td>3.54</td>
      <td>3.5</td>
      <td>0.79</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Load-Review-data-from-teh-Yelp-Academic-Dataset">Load Review data from teh Yelp Academic Dataset<a class="anchor-link" href="#Load-Review-data-from-teh-Yelp-Academic-Dataset">&#182;</a></h2>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[40]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">review_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;yelp_academic_dataset_review.csv&#39;</span><span class="p">)</span>
<span class="n">review_data</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[40]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>business_id</th>
      <th>cool</th>
      <th>date</th>
      <th>funny</th>
      <th>review_id</th>
      <th>stars</th>
      <th>text</th>
      <th>useful</th>
      <th>user_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>iCQpiavjjPzJ5_3gPD5Ebg</td>
      <td>0</td>
      <td>2011-02-25</td>
      <td>0.0</td>
      <td>x7mDIiDB3jEiPGPHOmDzyw</td>
      <td>2.0</td>
      <td>The pizza was okay. Not the best I've had. I p...</td>
      <td>0.0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>1</th>
      <td>pomGBqfbxcqPv14c3XH-ZQ</td>
      <td>0</td>
      <td>2012-11-13</td>
      <td>0.0</td>
      <td>dDl8zu1vWPdKGihJrwQbpw</td>
      <td>5.0</td>
      <td>I love this place! My fiance And I go here atl...</td>
      <td>0.0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>2</th>
      <td>jtQARsP6P-LbkyjbO1qNGg</td>
      <td>1</td>
      <td>2014-10-23</td>
      <td>1.0</td>
      <td>LZp4UX5zK3e-c5ZGSeo3kA</td>
      <td>1.0</td>
      <td>Terrible. Dry corn bread. Rib tips were all fa...</td>
      <td>3.0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>3</th>
      <td>elqbBhBfElMNSrjFqW3now</td>
      <td>0</td>
      <td>2011-02-25</td>
      <td>0.0</td>
      <td>Er4NBWCmCD4nM8_p1GRdow</td>
      <td>2.0</td>
      <td>Back in 2005-2007 this place was my FAVORITE t...</td>
      <td>2.0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ums3gaP2qM3W1XcA5r6SsQ</td>
      <td>0</td>
      <td>2014-09-05</td>
      <td>0.0</td>
      <td>jsDu6QEJHbwP2Blom1PLCA</td>
      <td>5.0</td>
      <td>Delicious healthy food. The steak is amazing. ...</td>
      <td>0.0</td>
      <td>msQe1u7Z_XuqjGoqhB0J5g</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[41]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">len</span><span class="p">(</span><span class="n">review_data</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[41]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>5996998</pre>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Subset to only food establishments</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[42]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">review_data</span> <span class="o">=</span> <span class="n">review_data</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">food_establishments</span><span class="p">,</span> <span class="n">on</span> <span class="o">=</span> <span class="s1">&#39;business_id&#39;</span><span class="p">,</span> <span class="n">how</span> <span class="o">=</span> <span class="s1">&#39;inner&#39;</span><span class="p">)</span>
<span class="nb">len</span><span class="p">(</span><span class="n">review_data</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[42]:</div>




<div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
<pre>3251200</pre>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[43]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">review_data</span> <span class="o">=</span> <span class="n">review_data</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">food_establishments</span><span class="p">,</span> <span class="n">on</span> <span class="o">=</span> <span class="s1">&#39;business_id&#39;</span><span class="p">,</span> <span class="n">how</span> <span class="o">=</span> <span class="s1">&#39;inner&#39;</span><span class="p">)</span>
<span class="n">filt_review</span> <span class="o">=</span> <span class="n">review_data</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;business_id&#39;</span><span class="p">])</span><span class="o">.</span><span class="n">agg</span><span class="p">({</span><span class="s1">&#39;review_id&#39;</span><span class="p">:</span> <span class="s1">&#39;count&#39;</span><span class="p">})</span>
<span class="n">food_review</span> <span class="o">=</span> <span class="n">food_establishments</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">filt_review</span><span class="p">,</span> <span class="n">on</span> <span class="o">=</span> <span class="s1">&#39;business_id&#39;</span><span class="p">,</span> <span class="n">how</span> <span class="o">=</span> <span class="s1">&#39;inner&#39;</span><span class="p">)</span>
<span class="n">food_review</span> <span class="o">=</span> <span class="n">food_review</span><span class="p">[[</span><span class="s1">&#39;business_id&#39;</span><span class="p">,</span> <span class="s1">&#39;review_count&#39;</span><span class="p">,</span> <span class="s1">&#39;review_id&#39;</span><span class="p">]]</span>
<span class="n">food_review</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;business_id&#39;</span><span class="p">:</span> <span class="s1">&#39;business_id&#39;</span><span class="p">,</span> <span class="s1">&#39;review_count&#39;</span><span class="p">:</span> <span class="s1">&#39;review_count&#39;</span><span class="p">,</span> <span class="s1">&#39;review_id&#39;</span><span class="p">:</span> <span class="s1">&#39;number_reviews&#39;</span><span class="p">},</span> <span class="n">inplace</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">food_review</span><span class="o">.</span><span class="n">tail</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[43]:</div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>business_id</th>
      <th>review_count</th>
      <th>number_reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>28633</th>
      <td>l1aseXzzr7Mu4SreSXp4pw</td>
      <td>21</td>
      <td>21</td>
    </tr>
    <tr>
      <th>28634</th>
      <td>h_CTVmgrnJdggumWd0wZPg</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>28635</th>
      <td>bQczh42duSfnETW-73xaTQ</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>28636</th>
      <td>HKP70vE8wFy-3fTO9jIm_w</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>28637</th>
      <td>ZUvhKyMAXVr98-4D4i36EQ</td>
      <td>21</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Text based analysis</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">excl</span> <span class="o">=</span> <span class="n">review_data</span><span class="p">[</span><span class="s1">&#39;text&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">extract</span><span class="p">(</span><span class="n">pat</span> <span class="o">=</span> <span class="sa">r</span><span class="s1">&#39;(!+)&#39;</span><span class="p">)</span>
<span class="n">excl</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">review_data</span><span class="p">,</span> <span class="n">excl</span><span class="p">],</span> <span class="n">axis</span> <span class="o">=</span> <span class="s1">&#39;columns&#39;</span><span class="p">)</span>
<span class="n">p21</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span> <span class="o">=</span> <span class="n">p21</span><span class="p">[[</span><span class="s1">&#39;stars&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">]]</span>
<span class="n">p21</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span><span class="p">[</span><span class="s1">&#39;exclamations&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">p21</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">len</span><span class="p">()</span>
<span class="n">p21</span><span class="p">[</span><span class="s1">&#39;exclamations&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">p21</span><span class="p">[</span><span class="s1">&#39;exclamations&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="c1">#p21[&#39;has_excl&#39;] = &#39;No&#39; if p21[&#39;exclamations&#39;] == 0 else &#39;Yes&#39;</span>
<span class="n">p21</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">&#39;exclamations&#39;</span><span class="p">,</span> <span class="n">ascending</span> <span class="o">=</span> <span class="kc">False</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span><span class="p">[</span><span class="s1">&#39;has_excl&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="kc">False</span> <span class="k">if</span> <span class="n">n</span> <span class="o">==</span> <span class="mi">0</span> <span class="k">else</span> <span class="kc">True</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">p21</span><span class="p">[</span><span class="s1">&#39;exclamations&#39;</span><span class="p">]]</span>
<span class="n">p21</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span><span class="p">[</span><span class="s1">&#39;exclamations&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">value_counts</span><span class="p">()</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;has_excl&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">agg</span><span class="p">({</span><span class="s1">&#39;stars&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;mean&#39;</span><span class="p">,</span> <span class="s1">&#39;std&#39;</span><span class="p">]})</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span> <span class="o">=</span> <span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span> <span class="o">=</span> <span class="s1">&#39;stars&#39;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="s1">&#39;exclamations&#39;</span><span class="p">,</span> <span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21_b</span> <span class="o">=</span> <span class="n">p21</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;stars&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">agg</span><span class="p">({</span><span class="s1">&#39;exclamations&#39;</span><span class="p">:</span> <span class="p">[</span><span class="s1">&#39;mean&#39;</span><span class="p">,</span> <span class="s1">&#39;std&#39;</span><span class="p">]})</span>
<span class="n">p21_b</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">inplace</span> <span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
<span class="n">p21_b</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">p21_b</span> <span class="o">=</span> <span class="n">p21_b</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
<span class="n">p21_b</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">kind</span> <span class="o">=</span> <span class="s1">&#39;scatter&#39;</span><span class="p">,</span> <span class="n">x</span> <span class="o">=</span> <span class="s1">&#39;stars&#39;</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="p">[(</span><span class="s1">&#39;exclamations&#39;</span><span class="p">,</span> <span class="s1">&#39;mean&#39;</span><span class="p">)],</span> <span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">5</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

     </div>
</div>
</div>
</div>

</div>
</body>







</html>
