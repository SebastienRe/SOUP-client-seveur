# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `Soup.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Soup
_M_Soup = Ice.openModule('Soup')
__name__ = 'Soup'

if '_t_songdatas' not in _M_Soup.__dict__:
    _M_Soup._t_songdatas = IcePy.defineSequence('::Soup::songdatas', (), IcePy._t_byte)

if 'Song' not in _M_Soup.__dict__:
    _M_Soup.Song = Ice.createTempClass()
    class Song(object):
        def __init__(self, id=0, title='', author='', extension='', type='', accuracy=0.0):
            self.id = id
            self.title = title
            self.author = author
            self.extension = extension
            self.type = type
            self.accuracy = accuracy

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_Soup.Song):
                return NotImplemented
            else:
                if self.id != other.id:
                    return False
                if self.title != other.title:
                    return False
                if self.author != other.author:
                    return False
                if self.extension != other.extension:
                    return False
                if self.type != other.type:
                    return False
                if self.accuracy != other.accuracy:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_Soup._t_Song)

        __repr__ = __str__

    _M_Soup._t_Song = IcePy.defineStruct('::Soup::Song', Song, (), (
        ('id', (), IcePy._t_int),
        ('title', (), IcePy._t_string),
        ('author', (), IcePy._t_string),
        ('extension', (), IcePy._t_string),
        ('type', (), IcePy._t_string),
        ('accuracy', (), IcePy._t_float)
    ))

    _M_Soup.Song = Song
    del Song

if '_t_Songs' not in _M_Soup.__dict__:
    _M_Soup._t_Songs = IcePy.defineSequence('::Soup::Songs', (), _M_Soup._t_Song)

_M_Soup._t_MusicLibrary = IcePy.defineValue('::Soup::MusicLibrary', Ice.Value, -1, (), False, True, None, ())

if 'MusicLibraryPrx' not in _M_Soup.__dict__:
    _M_Soup.MusicLibraryPrx = Ice.createTempClass()
    class MusicLibraryPrx(Ice.ObjectPrx):

        def addSong(self, title, author, type, extension, context=None):
            return _M_Soup.MusicLibrary._op_addSong.invoke(self, ((title, author, type, extension), context))

        def addSongAsync(self, title, author, type, extension, context=None):
            return _M_Soup.MusicLibrary._op_addSong.invokeAsync(self, ((title, author, type, extension), context))

        def begin_addSong(self, title, author, type, extension, _response=None, _ex=None, _sent=None, context=None):
            return _M_Soup.MusicLibrary._op_addSong.begin(self, ((title, author, type, extension), _response, _ex, _sent, context))

        def end_addSong(self, _r):
            return _M_Soup.MusicLibrary._op_addSong.end(self, _r)

        def addSongData(self, song, data, finish, context=None):
            return _M_Soup.MusicLibrary._op_addSongData.invoke(self, ((song, data, finish), context))

        def addSongDataAsync(self, song, data, finish, context=None):
            return _M_Soup.MusicLibrary._op_addSongData.invokeAsync(self, ((song, data, finish), context))

        def begin_addSongData(self, song, data, finish, _response=None, _ex=None, _sent=None, context=None):
            return _M_Soup.MusicLibrary._op_addSongData.begin(self, ((song, data, finish), _response, _ex, _sent, context))

        def end_addSongData(self, _r):
            return _M_Soup.MusicLibrary._op_addSongData.end(self, _r)

        def updateSong(self, song, reset, context=None):
            return _M_Soup.MusicLibrary._op_updateSong.invoke(self, ((song, reset), context))

        def updateSongAsync(self, song, reset, context=None):
            return _M_Soup.MusicLibrary._op_updateSong.invokeAsync(self, ((song, reset), context))

        def begin_updateSong(self, song, reset, _response=None, _ex=None, _sent=None, context=None):
            return _M_Soup.MusicLibrary._op_updateSong.begin(self, ((song, reset), _response, _ex, _sent, context))

        def end_updateSong(self, _r):
            return _M_Soup.MusicLibrary._op_updateSong.end(self, _r)

        def removeSong(self, song, context=None):
            return _M_Soup.MusicLibrary._op_removeSong.invoke(self, ((song, ), context))

        def removeSongAsync(self, song, context=None):
            return _M_Soup.MusicLibrary._op_removeSong.invokeAsync(self, ((song, ), context))

        def begin_removeSong(self, song, _response=None, _ex=None, _sent=None, context=None):
            return _M_Soup.MusicLibrary._op_removeSong.begin(self, ((song, ), _response, _ex, _sent, context))

        def end_removeSong(self, _r):
            return _M_Soup.MusicLibrary._op_removeSong.end(self, _r)

        def searchWithText(self, text, context=None):
            return _M_Soup.MusicLibrary._op_searchWithText.invoke(self, ((text, ), context))

        def searchWithTextAsync(self, text, context=None):
            return _M_Soup.MusicLibrary._op_searchWithText.invokeAsync(self, ((text, ), context))

        def begin_searchWithText(self, text, _response=None, _ex=None, _sent=None, context=None):
            return _M_Soup.MusicLibrary._op_searchWithText.begin(self, ((text, ), _response, _ex, _sent, context))

        def end_searchWithText(self, _r):
            return _M_Soup.MusicLibrary._op_searchWithText.end(self, _r)

        def playSong(self, song, context=None):
            return _M_Soup.MusicLibrary._op_playSong.invoke(self, ((song, ), context))

        def playSongAsync(self, song, context=None):
            return _M_Soup.MusicLibrary._op_playSong.invokeAsync(self, ((song, ), context))

        def begin_playSong(self, song, _response=None, _ex=None, _sent=None, context=None):
            return _M_Soup.MusicLibrary._op_playSong.begin(self, ((song, ), _response, _ex, _sent, context))

        def end_playSong(self, _r):
            return _M_Soup.MusicLibrary._op_playSong.end(self, _r)

        def stopSong(self, port, context=None):
            return _M_Soup.MusicLibrary._op_stopSong.invoke(self, ((port, ), context))

        def stopSongAsync(self, port, context=None):
            return _M_Soup.MusicLibrary._op_stopSong.invokeAsync(self, ((port, ), context))

        def begin_stopSong(self, port, _response=None, _ex=None, _sent=None, context=None):
            return _M_Soup.MusicLibrary._op_stopSong.begin(self, ((port, ), _response, _ex, _sent, context))

        def end_stopSong(self, _r):
            return _M_Soup.MusicLibrary._op_stopSong.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Soup.MusicLibraryPrx.ice_checkedCast(proxy, '::Soup::MusicLibrary', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Soup.MusicLibraryPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Soup::MusicLibrary'
    _M_Soup._t_MusicLibraryPrx = IcePy.defineProxy('::Soup::MusicLibrary', MusicLibraryPrx)

    _M_Soup.MusicLibraryPrx = MusicLibraryPrx
    del MusicLibraryPrx

    _M_Soup.MusicLibrary = Ice.createTempClass()
    class MusicLibrary(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Soup::MusicLibrary')

        def ice_id(self, current=None):
            return '::Soup::MusicLibrary'

        @staticmethod
        def ice_staticId():
            return '::Soup::MusicLibrary'

        def addSong(self, title, author, type, extension, current=None):
            raise NotImplementedError("servant method 'addSong' not implemented")

        def addSongData(self, song, data, finish, current=None):
            raise NotImplementedError("servant method 'addSongData' not implemented")

        def updateSong(self, song, reset, current=None):
            raise NotImplementedError("servant method 'updateSong' not implemented")

        def removeSong(self, song, current=None):
            raise NotImplementedError("servant method 'removeSong' not implemented")

        def searchWithText(self, text, current=None):
            raise NotImplementedError("servant method 'searchWithText' not implemented")

        def playSong(self, song, current=None):
            raise NotImplementedError("servant method 'playSong' not implemented")

        def stopSong(self, port, current=None):
            raise NotImplementedError("servant method 'stopSong' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Soup._t_MusicLibraryDisp)

        __repr__ = __str__

    _M_Soup._t_MusicLibraryDisp = IcePy.defineClass('::Soup::MusicLibrary', MusicLibrary, (), None, ())
    MusicLibrary._ice_type = _M_Soup._t_MusicLibraryDisp

    MusicLibrary._op_addSong = IcePy.Operation('addSong', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_Soup._t_Song, False, 0), ())
    MusicLibrary._op_addSongData = IcePy.Operation('addSongData', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Soup._t_Song, False, 0), ((), _M_Soup._t_songdatas, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    MusicLibrary._op_updateSong = IcePy.Operation('updateSong', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Soup._t_Song, False, 0), ((), IcePy._t_bool, False, 0)), (), None, ())
    MusicLibrary._op_removeSong = IcePy.Operation('removeSong', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Soup._t_Song, False, 0),), (), None, ())
    MusicLibrary._op_searchWithText = IcePy.Operation('searchWithText', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Soup._t_Songs, False, 0), ())
    MusicLibrary._op_playSong = IcePy.Operation('playSong', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Soup._t_Song, False, 0),), (), ((), IcePy._t_int, False, 0), ())
    MusicLibrary._op_stopSong = IcePy.Operation('stopSong', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, ())

    _M_Soup.MusicLibrary = MusicLibrary
    del MusicLibrary

# End of module Soup
